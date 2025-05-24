# gpt-pipeline-hub/Dockerfile
# ------------------------------------------
# Purpose:
#   Containerize the FastAPI evaluation pipeline for deployment on AWS AppRunner

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.lock requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files
COPY . /app

# Expose port for AppRunner
EXPOSE 8080

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
