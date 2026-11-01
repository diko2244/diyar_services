import os
import subprocess
import shutil
import uuid
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

# استيراد مكتبات التحويل
try:
    from pdf2docx import Converter
    HAS_PDF2DOCX = True
except ImportError:
    HAS_PDF2DOCX = False

try:
    from pdf2image import convert_from_path
    from pptx import Presentation
    from pptx.util import Inches
    HAS_PDF2PPT = True
except ImportError:
    HAS_PDF2PPT = False

app = Flask(__name__)
CORS(app)

# استخدام مجلد مؤقت داخل الحاوية
TEMP_DIR = "/tmp/converter"
os.makedirs(TEMP_DIR, exist_ok=True)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB

LIBREOFFICE_CONVERSIONS = {
    'docx': ['pdf', 'pptx'],
    'doc':  ['pdf', 'pptx'],
    'pptx': ['pdf', 'docx'],
    'ppt':  ['pdf', 'docx'],
}

def run_libreoffice(input_path, output_format, outdir):
    user_profile = os.path.join(outdir, 'lo_profile_' + uuid.uuid4().hex)
    cmd = [
        'libreoffice', '--headless', '--norestore', '--invisible',
        '--nodefault', '--nolockcheck',
        f'-env:UserInstallation=file://{user_profile}',
        '--convert-to', output_format,
        '--outdir', outdir,
        input_path
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
    except subprocess.TimeoutExpired:
        raise Exception("استغرق التحويل وقتاً طويلاً.")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8', errors='ignore')
        raise Exception(f"فشل LibreOffice: {error_msg}")
    
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(outdir, f"{base_name}.{output_format}")
    if not os.path.exists(output_path):
        raise Exception("لم يتم إنشاء الملف الناتج.")
    return output_path

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({"error": "لم يتم إرسال أي ملف"}), 400
    file = request.files['file']
    target_format = request.form.get('to', '').lower().strip()
    if not file.filename or not target_format:
        return jsonify({"error": "بيانات ناقصة"}), 400
    
    original_ext = os.path.splitext(file.filename)[1].lower().lstrip('.')
    if not original_ext:
        return jsonify({"error": "الملف بدون امتداد"}), 400
    
    job_id = uuid.uuid4().hex
    job_dir = os.path.join(TEMP_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)
    
    safe_name = secure_filename(file.filename) or f"input.{original_ext}"
    input_path = os.path.join(job_dir, safe_name)
    file.save(input_path)
    
    try:
        if original_ext == 'pdf' and target_format == 'docx':
            if not HAS_PDF2DOCX:
                return jsonify({"error": "pdf2docx غير متاح"}), 500
            output_path = os.path.join(job_dir, "output.docx")
            cv = Converter(input_path); cv.convert(output_path); cv.close()
        
        # التعديل الجديد: تحويل PDF إلى PowerPoint كصور
        elif original_ext == 'pdf' and target_format == 'pptx':
            if not HAS_PDF2PPT:
                return jsonify({"error": "مكتبات pdf2image أو python-pptx غير متاحة"}), 500
            
            # تحويل كل صفحة PDF إلى صورة
            images = convert_from_path(input_path)
            prs = Presentation()
            blank_slide_layout = prs.slide_layouts[6]
            
            for img in images:
                slide = prs.slides.add_slide(blank_slide_layout)
                img_path = os.path.join(job_dir, f"slide_{uuid.uuid4().hex}.jpg")
                img.save(img_path, "JPEG")
                # تغطية الشريحة بالكامل بالصورة
                slide.shapes.add_picture(img_path, 0, 0, width=prs.slide_width, height=prs.slide_height)
            
            output_path = os.path.join(job_dir, "output.pptx")
            prs.save(output_path)
        
        elif original_ext in LIBREOFFICE_CONVERSIONS and target_format in LIBREOFFICE_CONVERSIONS[original_ext]:
            output_path = run_libreoffice(input_path, target_format, job_dir)
        else:
            return jsonify({"error": f"التحويل من {original_ext} إلى {target_format} غير مدعوم"}), 400
        
        if output_path and os.path.exists(output_path):
            return send_file(output_path, as_attachment=True, download_name=f"converted.{target_format}")
        return jsonify({"error": "فشل إنشاء الملف"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        import threading, time
        def cleanup():
            time.sleep(5)
            shutil.rmtree(job_dir, ignore_errors=True)
        threading.Thread(target=cleanup, daemon=True).start()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)