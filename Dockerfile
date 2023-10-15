# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install the required libraries (watchdog and putio.py)
RUN pip install watchdog putio.py

# Copy your Python script into the container
COPY monitor_torrents.py .

# Run your script when the container starts
CMD ["python", "monitor_torrents.py"]
