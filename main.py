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
from flask import Flask

from views.home import (
    home_view,
    contact_view,
)
from views.employee import (
    employee_list_view,
    employee_add_view,
    employee_edit_view,
    employee_delete_view,
    employee_list_api,
    employee_api,
)

app = Flask(__name__)
app.secret_key = b"bEB2PeOgX3FAOtuUUakN5h9eNDyL5vLoAMz3ZkpC7vE"

# @app.route() lets you set the url path that will trigger each view.
# '/' is the root of the domain. If your website was hosted at example.com
# then the full url would be https://example.com/
# If the path was '/do/thing/' then the full url would be https://example.com/do/thing/
app.add_url_rule("/", view_func=home_view)
app.add_url_rule("/contact", view_func=contact_view)
# Employee routes
app.add_url_rule("/employees", view_func=employee_list_view)
app.add_url_rule(
    "/employees/add",
    view_func=employee_add_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/employees/<int:pk>/edit",
    view_func=employee_edit_view,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/employees/<int:pk>/delete",
    view_func=employee_delete_view,
    methods=["GET", "POST"],
)

# Add some API endpoints that return our database data as JSON
app.add_url_rule(
    "/api/employees",
    view_func=employee_list_api,
)

app.add_url_rule(
    "/api/employees/<int:pk>",
    view_func=employee_api,
)
