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


def employee_add_view():
    """Show page for adding a new Employee / accept form data"""
    errors = []
    first_name = ""
    last_name = ""
    weekly_salary = ""
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        weekly_salary = request.form["weekly_salary"]

        if not first_name:
            errors.append("The First Name is required")
        if not last_name:
            errors.append("The Last Name is required")
        if not weekly_salary:
            errors.append("The Weekly Salary is required")
        try:
            float(weekly_salary)
        except ValueError:
            errors.append("The Weekly Salary must be a float")

        if not errors:
            new_employee = Employee(first_name, last_name, weekly_salary)
            db_session.add(new_employee)
            db_session.commit()

            flash("User added successfully")

            return redirect(url_for("employee_list_view"))

    return render_template(
        "employee/employee_add.html",
        errors=errors,
        first_name=first_name,
        last_name=last_name,
        weekly_salary=weekly_salary,
    )
