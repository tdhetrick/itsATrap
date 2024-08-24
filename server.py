from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory log for simplicity. In a real scenario, you might want to log to a file or database.
log = []

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
    log.append(log_entry)

    # Log the attempt to the console (or log file in a real scenario)
    print(f"[*] Honeypot hit by {user_ip}")
    print(f"[*] User-Agent: {user_agent}")
    print(f"[*] Username: {username}")
    print(f"[*] Password: {password}")

    # Redirect to a fake "Login Failed" page
    return redirect(url_for('login_failed'))

@app.route('/login_failed')
def login_failed():
    return render_template('login_failed.html')

@app.route('/logs')
def show_logs():
    return render_template('logs.html', log=log)

if __name__ == '__main__':
    app.run(debug=True)
