# Use the official lightweight Python image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000
EXPOSE 8000

# Run command (ensure the path to main is correct)
# If app is in the root directory: main:app
# If inside an app folder: app.main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]