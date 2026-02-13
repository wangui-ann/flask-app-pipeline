from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    secret = os.environ.get("SECRET_KEY", "NoSecret")
    return f"Hello World... Secret: {secret}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
