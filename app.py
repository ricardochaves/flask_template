import logging

from flask import Flask
from flask import url_for

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/", methods=["GET"])
def hello():

    # methods=['GET', 'POST']
    return "Hello World!"


@app.route("/user/<username>")
def user(username):
    post_url = url_for("show_post", post_id=2)
    return f"I'm {username} and url for your first post is {post_url}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return "Subpath %s" % subpath


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return "Post %d" % post_id
