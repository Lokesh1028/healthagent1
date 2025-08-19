FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file (from backend directory)
COPY ./backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application files
COPY ./backend/ .

# Create directories that might be needed
RUN mkdir -p /app/vector_db

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]
