from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
  return jsonify({
      "author":
      "Phạm Quốc Cường",
      "link":
      "https://www.facebook.com/profile.php?id=100063050334248"
  })

@app.errorhandler(404)
def not_found(error):
  return jsonify({
      "author":
      "Phạm Quốc Cường",
      "link":
      "https://www.facebook.com/profile.php?id=100063050334248"
  }), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0')
