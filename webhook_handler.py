#!/usr/bin/env python3
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Validate the incoming request if necessary
    # Parse the payload if required

    # Run the Ansible playbook command
    result = subprocess.run(['ansible-playbook', 'simpleplaybook.yml'], capture_output=True)

    if result.returncode == 0:
        return 'Playbook executed successfully', 200
    else:
        return 'Playbook execution failed', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
