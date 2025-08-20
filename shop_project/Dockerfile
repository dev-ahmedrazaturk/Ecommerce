# Use an official Python runtime as a parent image
FROM python:3.13.1

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app will run on (default Django port)
EXPOSE 8000

# Make sure the static files directory is created when container starts
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Set environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=shop_project.settings

# Run the application, make sure it listens on all IP addresses (0.0.0.0)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
