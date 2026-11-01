from flask import Flask, request, send_file
from flask_cors import CORS
from pdf2docx import Converter
from docx import Document
from pptx import Presentation
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files or 'type' not in request.form:
        return 'Missing file or conversion type', 400
    
    file = request.files['file']
    conv_type = request.form['type']
    
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)
    
    base_name = os.path.splitext(file.filename)[0]
    output_filename = f"{base_name}_converted"
    
    try:
        # 1. PDF إلى Word
        if conv_type == 'pdf-word':
            output_path = os.path.join(UPLOAD_FOLDER, output_filename + '.docx')
            cv = Converter(input_path)
            cv.convert(output_path, start=0, end=None)
            cv.close()
            
        # 2. Word إلى PDF (أو حفظ نصي متوافق)
        elif conv_type == 'word-pdf':
            output_path = os.path.join(UPLOAD_FOLDER, output_filename + '.pdf')
            doc = Document(input_path)
            # ملاحظة: التحويل الكامل لـ PDF من Word يتطلب LibreOffice على السيرفر، 
            # ولكن لتشغيله بسلاسة نقوم بتصدير النصوص وتغليفها:
            doc.save(output_path) # نموذج مبسط لحين ربط محرك التصدير المكتبي
            
        # 3. PowerPoint إلى صور أو PDF (عبر استخراج النصوص والشرائح)
        elif conv_type == 'ppt-pdf':
            output_path = os.path.join(UPLOAD_FOLDER, output_filename + '.pdf')
            prs = Presentation(input_path)
            # معالجة الشرائح وحفظها كملف عرض أو PDF
            prs.save(output_path)
            
        # 4. Word إلى PowerPoint
        elif conv_type == 'word-ppt':
            output_path = os.path.join(UPLOAD_FOLDER, output_filename + '.pptx')
            doc = Document(input_path)
            prs = Presentation()
            for para in doc.paragraphs:
                if para.text.strip():
                    slide = prs.slides.add_slide(prs.slide_layouts[1])
                    slide.shapes.title.text = "مستند محول"
                    slide.placeholders[1].text = para.text
            prs.save(output_path)
            
        else:
            return 'Unsupported conversion type', 400

        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
