FROM registry-1.docker.io/library/python:3.11-slim


WORKDIR /app

# Copy app and templates
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir flask requests

EXPOSE 5000

CMD ["python", "app.py"]
