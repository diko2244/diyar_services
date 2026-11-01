# استخدام صورة أوبنتو الرسمية
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# تثبيت LibreOffice والخطوط العربية والأدوات المطلوبة
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    libreoffice \
    libreoffice-writer \
    libreoffice-impress \
    libreoffice-calc \
    fonts-liberation \
    fonts-noto \
    fonts-kacst \
    fonts-hosny-amiri \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--threads", "4", "--timeout", "180", "app:app"]