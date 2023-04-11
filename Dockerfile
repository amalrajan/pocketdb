# Use the Ubuntu latest image as the base image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Update package lists and install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install requirements
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy the Flask app files to the container
COPY datastore/* /app/

# Expose the port that the Flask app will run on
EXPOSE 8080

# Start the app
CMD ["python3", "main.py"]
