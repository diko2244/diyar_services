FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
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

# بيئة افتراضية: تحل PEP 668 وتضمن أن pip و gunicorn من نفس البيئة
RUN python3 -m venv "$VIRTUAL_ENV"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--workers", "1", "--threads", "4", "--timeout", "180", "app:app"]