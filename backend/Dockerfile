FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create vector_db directory
RUN mkdir -p /app/vector_db

# Expose port
EXPOSE 8000

# Start the application
CMD ["python", "main.py"]
