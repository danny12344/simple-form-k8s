# Use a base image that includes Python and other dependencies
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Install pip
RUN apt-get update && apt-get install -y python3-pip && pip3 install --upgrade pip

COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV HOST=0.0.0.0
ENV PORT=8080

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
