"""Tiny Flask Example

From https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart

Requires you to install flask in your virtual environment:

  $ . .venv/Scripts/activate

  $ python -m pip install flask

To run this on windows:

  Activate your environment if you haven't already.

  $ flask --app main run

Then in a browser go to http://127.0.0.1:5000/
"""
from flask import (
    Flask,
    render_template,
)


app = Flask(__name__)


# @app.route() lets you set the url path that will trigger each view.
# '/' is the root of the domain. If your website was hosted at example.com
# then the full url would be https://example.com/
# If the path was '/do/thing/' then the full url would be https://example.com/do/thing/
@app.route("/")
def home():
    # Return the home template page
    return render_template("home.html")


@app.route("/contact")
def contact():
    # Return the contact template page.
    return render_template("contact.html")
