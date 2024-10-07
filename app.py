from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins=["https://llama-chat-snowy.vercel.app", "http://localhost:5173"])

@app.route('/hello')
def hello_world():  # put application's code here
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run()
