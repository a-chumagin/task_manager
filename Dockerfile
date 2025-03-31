FROM python:3.10

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies using pip (simplifying to avoid credential issues)
RUN pip install --no-cache-dir -r requirements.txt

# Install uv package manager
RUN pip install --no-cache-dir uv

# Copy the rest of the application
COPY . .

# Create data directory
RUN mkdir -p /app/data

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]