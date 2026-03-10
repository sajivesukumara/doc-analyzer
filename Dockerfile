from docker.io/library/python:3.11-slim-bullseye

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
# curl: for networking
# tesseract-ocr: the engine
# libgl1: required for OpenCV (cv2) to run in a headless environment
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    tesseract-ocr \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY reqirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py",  "book_image.png"]

