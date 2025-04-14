# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    graphviz \
    pylint \
    git \
    build-essential \
    && pip install --no-cache-dir --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create app directory
WORKDIR /workspace

# Copy code
COPY . .

# Run tests and coverage during build (optional)
# RUN ./run-unit-tests-and-coverage.sh

CMD ["bash"]
