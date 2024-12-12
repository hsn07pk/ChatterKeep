# Use a specific version of Python as base image
FROM python:3.10.10

# Metadata for the image
LABEL maintainer="Hassan <hsn07pk@gmail.com>"
LABEL version="1.0"
LABEL description="A Flask-based chatbot application with multi-user session management."

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app

# Install dependencies and curl (for health check)
RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5000

# Health check to ensure the application is running
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 CMD curl --fail http://localhost:5000 || exit 1

# Command to start the Flask app (adjusted to use flask CLI for production)
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
