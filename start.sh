#!/bin/bash

# Start the Flask app
python3 server.py &

# Start another application (e.g., a background job or another service)
# Replace with your own command
#another_command &

# Optional: Start a service like cron or any other service
#service cron start &

# Keep the container running
tail -f /dev/null
