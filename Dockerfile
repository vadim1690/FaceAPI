# Use a lightweight Python image
FROM python:3.10-slim

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk2.0-dev \
    libboost-python-dev \
    libssl-dev \
    && apt-get clean

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
