# 1. تحميل بيئة بايثون
FROM python:3.11-slim

# 2. تثبيت برنامج LibreOffice + خطوط عربية وكوردية
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice-writer \
    libreoffice-impress \
    libreoffice-calc \
    fonts-liberation \
    fonts-noto \
    fonts-noto-core \
    fonts-noto-extra \
    fonts-kacst \
    fonts-hosny-amiri \
    fonts-sil-scheherazade \
    && rm -rf /var/lib/apt/lists/*

# 3. إنشاء مجلد العمل
WORKDIR /app

# 4. نسخ ملف المتطلبات وتثبيت مكتبات بايثون
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. نسخ باقي ملفات المشروع
COPY . .

# 6. فتح المنفذ وتشغيل السيرفر
EXPOSE 10000
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--threads", "4", "--timeout", "180", "app:app"]