# Use an official Python runtime as a parent image
FROM python:3.13.1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN pip install Pillow

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Django to run on
EXPOSE 8000

# Run migrations and then start the Django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
