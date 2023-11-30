# Third-party Imports
from flask import (
    flash,
    render_template,
    request,
    redirect,
    url_for,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# First-party Imports
from models.employee import Employee

# Set up SQLAlchemy stuff
engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
db_session = Session()


def employee_list_view():
    """Display a list of employees from the database"""
    employees = db_session.query(Employee).all()

    return render_template(
        "employee/employee_list.html",
        employees=employees,
    )
