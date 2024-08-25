# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Flask app to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy the start script
COPY start.sh /app/start.sh

# Expose the port Flask will run on
EXPOSE 5000

# Run the start script
ENTRYPOINT ["/app/start.sh"]


# docker build -t Honey.Dockerfile .
# docker run -d -p 5000:5000 Honey.Dockerfile