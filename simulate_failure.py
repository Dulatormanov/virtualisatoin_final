import os
from flask import Flask

app = Flask(__name__)

@app.route('/healthz')
def health():
    if os.getenv('SIMULATE_FAILURE') == 'true':
        return "Failure simulated", 500
    return "Healthy", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
