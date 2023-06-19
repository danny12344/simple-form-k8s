# Use a base image that includes Python and other dependencies
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Install pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip

# Install Nginx and other necessary packages
RUN apt-get install -y nginx

# Remove the default NGINX configuration
RUN rm -f /etc/nginx/conf.d/default.conf

# Copy the application code to the container
COPY index.html .
COPY script.js .

# Copy your modified Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Copy your HTML and JS files to the appropriate directory
COPY index.html /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the host and port for the FastAPI application
ENV HOST=0.0.0.0
ENV PORT=80

# Expose the port on which the FastAPI application will run
EXPOSE 80

# Start Nginx service
CMD ["nginx", "-g", "daemon off;"]
# Set the command to start the FastAPI application - is this needed?
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
