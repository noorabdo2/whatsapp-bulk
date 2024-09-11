from flask import Flask, request, jsonify, send_from_directory
import pywhatkit as kit
import time
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data['sender']
    message = data['message']
    recipients = data['recipients']

    for recipient in recipients:
        try:
            kit.sendwhatmsg_instantly(f"+{recipient.strip()}", message)
            time.sleep(10)  # To avoid being blocked by WhatsApp
        except Exception as e:
            return jsonify({'message': f'Failed to send message to {recipient}: {str(e)}'}), 500

    return jsonify({'message': 'Messages sent successfully!'})

if __name__ == '__main__':
    app.run(port=5000)