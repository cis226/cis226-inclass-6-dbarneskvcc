from flask import render_template


def home_view():
    # Return the home template page
    return render_template("home.html")


def contact_view():
    # Return the contact template page.
    return render_template("contact.html")
