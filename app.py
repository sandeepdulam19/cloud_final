from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()

# Safely resolve IP or fallback to 'Unavailable'
try:
    ip_address = socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address = 'Unavailable'

@app.route('/')
def hello_cloud():
    return "Welcome to Dulam Final Test API Server"

@app.route('/host')
def host_name():
    return hostname

@app.route('/ip')
def host_ip():
    return ip_address

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
