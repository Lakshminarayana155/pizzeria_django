FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt




# # Build stage
# FROM python:3.11 AS builder

# # Set working directory in the builder stage
# WORKDIR /build

# # Install system libraries needed for gobject-2.0-0
# # RUN apt-get update && apt-get install -y libgirepository1.0-dev gir1.2-glib-2.0

# # Copy only the requirements file to leverage Docker caching
# COPY requirements.txt .

# # Install dependencies in the builder stage
# RUN pip install --no-cache-dir -r requirements.txt

# # Runtime stage
# FROM python:3.11-slim

# # environment variable ensures that the Python output is set straight to the terminal without buffering it first
# ENV PYTHONUNBUFFERED 1

# # Install system libraries needed for gobject-2.0-0 in the runtime stage
# # RUN apt-get update && apt-get install -y libglib2.0-0 libpango-1.0-0 libpangoft2-1.0-0

# # Set working directory in the final runtime stage
# WORKDIR /app

# # Copy only the necessary files from the builder stage to the final runtime stage
# COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# # Copy the rest of your application code to the container
# COPY . /app/

# WORKDIR /app/pizzeria

# EXPOSE 8000

# # CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["sh", "-c", "celery -A pizzeria.celery worker --pool=solo -l info & celery -A pizzeria.celery beat -l info & python manage.py runserver 0.0.0.0:8000"]
