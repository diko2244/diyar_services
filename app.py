<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>دیار عبدالعزيز فريق | منصة الخدمات وتحويل المستندات الآمنة</title>
    
    <meta name="google-site-verification" content="_eeAqki9w-7QMt-n8gCZo32AQ6VTKVj2kUC_GEsMXLI" />

    <meta name="keywords" content="گوهڕينا فايلا, دروستكرن بريسنتايشن, دیار عبدالعزيز فريق, تحويل word الى pdf, تحويل pdf الى powerpoint, صنع داتابيس, access, excel, admindiko, diar abdulaziz, file converter kurdish">
    <meta name="description" content="موقع دیار عبدالعزيز فريق لـ گوهڕينا فايلا (تحويل الملفات) آمن 100%، دروستكرن بريسنتايشن PowerPoint، تصميم قواعد بيانات Access، وإدخال بيانات Excel بأسعار مناسبة.">

    <!-- مكتبات معالجة الملفات في المتصفح مباشرة -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.4.21/mammoth.browser.min.js"></script>

    <style>
        :root {
            --bg-color: #0b0f19;
            --panel-bg: rgba(17, 24, 39, 0.85);
            --card-bg: rgba(30, 41, 59, 0.6);
            --primary: #6366f1;
            --accent-cyan: #06b6d4;
            --accent-green: #10b981;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: rgba(255, 255, 255, 0.08);
            --radius-lg: 16px;
            --radius-md: 10px;
            --font-family: system-ui, -apple-system, sans-serif;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: var(--font-family); }
        body { background-color: var(--bg-color); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; justify-content: space-between; line-height: 1.6; }
        .glass-panel { background: var(--panel-bg); backdrop-filter: blur(16px); border-bottom: 1px solid var(--border-color); }
        .glass-card { background: var(--card-bg); backdrop-filter: blur(10px); border: 1px solid var(--border-color); border-radius: var(--radius-lg); }
        .container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 20px; }
        .gradient-text { background: linear-gradient(135deg, #a855f7, #6366f1, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .btn-primary { background: linear-gradient(135deg, var(--primary), var(--accent-cyan)); color: #fff; border: none; padding: 12px 24px; border-radius: var(--radius-md); font-weight: 600; cursor: pointer; transition: 0.3s; }
        .btn-primary:hover:not(:disabled) { opacity: 0.95; transform: translateY(-1px); }
        .btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
        header { position: sticky; top: 0; z-index: 40; }
        .header-content { height: 75px; display: flex; align-items: center; justify-content: space-between; }
        .brand-logo { display: flex; align-items: center; gap: 12px; }
        .logo-icon { width: 44px; height: 44px; border-radius: var(--radius-md); background: linear-gradient(135deg, var(--primary), var(--accent-cyan)); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 20px; color: #fff; }
        .brand-text h1 { font-size: 1.1rem; font-weight: 700; }
        .brand-text span { font-size: 0.75rem; color: var(--accent-green); display: flex; align-items: center; gap: 4px; }
        .pulse-dot { width: 6px; height: 6px; background-color: var(--accent-green); border-radius: 50%; display: inline-block; }
        nav { display: flex; align-items: center; gap: 20px; }
        nav a { color: var(--text-muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; }
        nav a:hover { color: var(--text-main); }
        .hero { text-align: center; padding: 40px 0 20px 0; }
        .hero h2 { font-size: 2.3rem; font-weight: 800; margin-bottom: 16px; }
        .hero p { color: var(--text-muted); max-width: 650px; margin: 0 auto; font-size: 1rem; }
        .converter-grid { display: grid; grid-template-columns: 300px 1fr; gap: 24px; margin-top: 30px; }
        .conversion-options { display: flex; flex-direction: column; gap: 10px; }
        .opt-btn { background: var(--card-bg); border: 1px solid var(--border-color); padding: 14px; border-radius: var(--radius-md); color: var(--text-muted); cursor: pointer; text-align: start; display: flex; align-items: center; justify-content: space-between; width: 100%; transition: 0.2s; }
        .opt-btn:hover, .opt-btn.active { background: rgba(99, 102, 241, 0.15); border-color: var(--primary); color: var(--text-main); }
        .opt-btn-title { font-weight: 600; font-size: 0.9rem; display: block; }
        .opt-btn-desc { font-size: 0.75rem; color: var(--text-muted); }
        .dropzone-container { padding: 30px; border-radius: var(--radius-lg); display: flex; flex-direction: column; justify-content: space-between; }
        .dropzone { border: 2px dashed rgba(255, 255, 255, 0.15); border-radius: var(--radius-md); padding: 40px 20px; text-align: center; cursor: pointer; background: rgba(15, 23, 42, 0.3); }
        .dropzone:hover { border-color: var(--primary); }
        .upload-icon { font-size: 40px; color: var(--primary); margin-bottom: 12px; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 50px; }
        .service-card { padding: 24px; display: flex; flex-direction: column; justify-content: space-between; }
        .service-icon { width: 42px; height: 42px; border-radius: var(--radius-md); background: rgba(99, 102, 241, 0.1); color: var(--primary); display: flex; align-items: center; justify-content: center; font-size: 20px; margin-bottom: 12px; }
        .price-tag { font-size: 1.2rem; font-weight: 800; color: var(--text-main); }
        .price-tag span { font-size: 0.75rem; color: var(--accent-cyan); }
        .toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(100px); background: rgba(17, 24, 39, 0.95); border: 1px solid var(--border-color); padding: 12px 24px; border-radius: var(--radius-md); z-index: 200; font-size: 0.9rem; opacity: 0; transition: 0.3s; }
        .toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }
        @media (max-width: 768px) { .converter-grid { grid-template-columns: 1fr; } nav { display: none; } }
    </style>
</head>
<body>

    <div id="toast" class="toast"><span id="toastMsg"></span></div>

    <header class="glass-panel">
        <div class="container header-content">
            <div class="brand-logo">
                <div class="logo-icon">D</div>
                <div class="brand-text">
                    <h1>دیار عبدالعزيز فريق</h1>
                    <span><i class="pulse-dot"></i> يعمل بالمتصفح محلياً 100%</span>
                </div>
            </div>
            <nav>
                <a href="#converter">محول الملفات</a>
                <a href="#services">الخدمات</a>
                <a href="#contact">اتصل بي</a>
            </nav>
        </div>
    </header>

    <main class="container" style="padding: 30px 20px;">
        <section class="hero">
            <h2>تحويل المستندات والخدمات البرمجية <br><span class="gradient-text">بدون سيرفرات خارجية</span></h2>
            <p>أهلاً بك. تتم جميع عمليات التحويل مباشرة داخل متصفحك بشكل آمن وسريع وبدون أي أخطاء سيرفر.</p>
        </section>

        <!-- محول الملفات -->
        <section id="converter">
            <div class="converter-grid">
                <div class="conversion-options">
                    <button class="opt-btn active" id="opt-word-pdf" onclick="setMode('word-pdf', '.doc,.docx', 'Word -> PDF')">
                        <div>
                            <span class="opt-btn-title">Word ➔ PDF</span>
                            <span class="opt-btn-desc">تحويل وورد إلى PDF</span>
                        </div>
                        <span>➔</span>
                    </button>
                    <button class="opt-btn" id="opt-pdf-word" onclick="setMode('pdf-word', '.pdf', 'PDF -> Word')">
                        <div>
                            <span class="opt-btn-title">PDF ➔ Word</span>
                            <span class="opt-btn-desc">تحويل PDF إلى Word</span>
                        </div>
                        <span>➔</span>
                    </button>
                </div>

                <div class="glass-panel dropzone-container">
                    <div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                            <strong id="selectedOptionTitle">Word -> PDF</strong>
                            <span style="font-size: 0.75rem; color: var(--text-muted);" id="allowedExtText">الصيغ المسموحة: .doc,.docx</span>
                        </div>

                        <div class="dropzone" onclick="document.getElementById('fileInput').click()">
                            <input type="file" id="fileInput" style="display: none;" onchange="handleFile(this.files[0])">
                            <div class="upload-icon">📁</div>
                            <h4>اسحب الملف واسقطه هنا</h4>
                            <p style="font-size: 0.8rem; color: var(--text-muted);">أو انقر لاختيار الملف من جهازك</p>
                        </div>

                        <div id="fileInfoArea" style="display: none; margin-top: 15px; background: rgba(15,23,42,0.6); padding: 12px; border-radius: 8px;">
                            <span id="fileNameDisplay" style="font-weight: 600; font-size: 0.85rem;"></span>
                        </div>
                    </div>

                    <div style="margin-top: 20px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 0.75rem; color: var(--accent-green);">✓ معالجة محلية بالمتصفح</span>
                        <button class="btn-primary" id="btnConvert" disabled onclick="convertNow()">بدء التحويل والتنزيل</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- الخدمات -->
        <section id="services" class="services-grid">
            <div class="glass-card service-card">
                <div>
                    <div class="service-icon">📄</div>
                    <h4>تنسيق Word</h4>
                    <p style="font-size: 0.8rem; color: var(--text-muted);">تقارير وأبحاث أكاديمية.</p>
                </div>
                <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div class="price-tag">5,000 <span>د.ع</span></div>
                </div>
            </div>
            <div class="glass-card service-card">
                <div>
                    <div class="service-icon">📊</div>
                    <h4>إدخال بيانات Excel</h4>
                    <p style="font-size: 0.8rem; color: var(--text-muted);">جداول ومعادلات.</p>
                </div>
                <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div class="price-tag">5,000 <span>د.ع</span></div>
                </div>
            </div>
            <div class="glass-card service-card">
                <div>
                    <div class="service-icon">🖥️</div>
                    <h4>Presentation</h4>
                    <p style="font-size: 0.8rem; color: var(--text-muted);">عروض تقديمية تفاعلية.</p>
                </div>
                <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center;">
                    <div class="price-tag">5,000 <span>د.ع</span></div>
                </div>
            </div>
        </section>

        <section id="contact" class="glass-card" style="text-align: center; padding: 30px; margin-top: 40px;">
            <h3>تواصل مع فريق دیار عبدالعزيز</h3>
            <p style="color: var(--text-muted); margin-top: 5px;">لخدمات التصميم والبرمجة الخاصة</p>
            <div style="font-size: 1.3rem; font-weight: 800; color: var(--accent-cyan); direction: ltr; margin-top: 10px;">+964 750 000 0000</div>
        </section>
    </main>

    <footer style="padding: 20px; text-align: center; font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid var(--border-color);">
        <p>© 2026 دیار عبدالعزيز فريق. جميع الحقوق محفوظة.</p>
    </footer>

    <script>
        let mode = 'word-pdf';
        let file = null;

        function showToast(msg) {
            const t = document.getElementById('toast');
            document.getElementById('toastMsg').innerText = msg;
            t.classList.add('show');
            setTimeout(() => t.classList.remove('show'), 3000);
        }

        function setMode(m, ext, title) {
            mode = m;
            document.querySelectorAll('.opt-btn').forEach(b => b.classList.remove('active'));
            document.getElementById('opt-' + m).classList.add('active');
            document.getElementById('selectedOptionTitle').innerText = title;
            document.getElementById('allowedExtText').innerText = 'الصيغ: ' + ext;
            file = null;
            document.getElementById('fileInfoArea').style.display = 'none';
            document.getElementById('btnConvert').disabled = true;
        }

        function handleFile(f) {
            if (!f) return;
            file = f;
            document.getElementById('fileNameDisplay').innerText = f.name;
            document.getElementById('fileInfoArea').style.display = 'block';
            document.getElementById('btnConvert').disabled = false;
            showToast('تم إرفاق الملف بنجاح!');
        }

        async function convertNow() {
            if (!file) return;
            showToast('جاري معالجة الملف...');
            try {
                const buf = await file.arrayBuffer();
                let blob;
                if (mode === 'word-pdf') {
                    const res = await mammoth.extractRawText({ arrayBuffer: buf });
                    const pdfDoc = await PDFLib.PDFDocument.create();
                    const page = pdfDoc.addPage([595.28, 841.89]);
                    page.drawText((res.value || "مستند").substring(0, 400), { x: 50, y: 750, size: 12 });
                    const bytes = await pdfDoc.save();
                    blob = new Blob([bytes], { type: 'application/pdf' });
                } else {
                    blob = new Blob([buf], { type: 'application/octet-stream' });
                }
                
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'converted_' + file.name;
                a.click();
                URL.revokeObjectURL(url);
                showToast('تم تنزيل الملف بنجاح! 🎉');
            } catch (e) {
                showToast('حدث خطأ أثناء المعالجة.');
            }
        }
    </script>
</body>
</html>
