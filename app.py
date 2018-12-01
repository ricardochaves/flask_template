import logging

from flask import Flask
from flask import jsonify

import requests

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"])
def hello():
    app.logger.info("Home executed.")
    return "Hello World!"


@app.route("/githubuser/<string:username>")
def user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    return jsonify({"urser_name": username, "id": response.json()["id"], "created_at": response.json()["created_at"]})


@app.route("/path/<path:subpath>")
def show_subpath(subpath):

    return jsonify({"your_path": subpath})
