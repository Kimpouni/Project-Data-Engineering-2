from flask import Flask, request, jsonify
from flask_cors import CORS

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText

app = Flask(__name__)
CORS(app)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')