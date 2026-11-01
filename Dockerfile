# استخدام صورة Python رسمية خفيفة
FROM python:3.11-slim

# تثبيت LibreOffice والخطوط الأساسية
RUN apt-get update && apt-get install -y --no-install-recommends \
    libreoffice-writer \
    libreoffice-impress \
    libreoffice-calc \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

# تعيين مجلد العمل
WORKDIR /app

# نسخ ملفات المتطلبات وتثبيتها أولاً (لاستغلال التخزين المؤقت)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تعريض المنفذ الذي سيستمع عليه Render
EXPOSE 10000

# تشغيل السيرفر باستخدام Gunicorn (مثالي لـ Render)
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--threads", "4", "--timeout", "180", "app:app"]