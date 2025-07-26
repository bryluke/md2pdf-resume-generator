FROM python:3.11-slim

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy application code
COPY . .

ENTRYPOINT ["python", "main.py"]
