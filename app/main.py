from flask import Flask
from dotenv import load_dotenv
import os

# Take environment variables from .env.
load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)