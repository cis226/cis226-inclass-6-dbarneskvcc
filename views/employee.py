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
            weekly_salary = float(weekly_salary)
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


def employee_edit_view(pk):
    """Show page for editing an existing Employee"""

    errors = []

    employee = db_session.get(Employee, pk)

    if not employee:
        errors.append(f"Unknown employee with pk of {pk}")

    if employee and request.method == "POST":
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
            weekly_salary = float(weekly_salary)
        except ValueError:
            errors.append("The Weekly Salary must be a float")

        if not errors:
            employee.first_name = first_name
            employee.last_name = last_name
            employee.weekly_salary = weekly_salary
            db_session.commit()

            flash("User updated successfully")

            return redirect(url_for("employee_list_view"))

    return render_template(
        "employee/employee_edit.html",
        errors=errors,
        employee=employee,
    )


def employee_delete_view(pk):
    """Show page for deleting an existing Employee"""

    errors = []

    employee = db_session.get(Employee, pk)

    if not employee:
        errors.append(f"Unknown employee with pk of {pk}")

    if employee and request.method == "POST":
        db_session.delete(employee)
        db_session.commit()

        flash("User deleted successfully")

        return redirect(url_for("employee_list_view"))

    return render_template(
        "employee/employee_delete.html",
        errors=errors,
        employee=employee,
    )


def employee_list_api():
    """Returns JSON of employees from the database"""
    employees = db_session.query(Employee).all()

    # Convert employee instances to dicts inside a list.
    return [e.to_dict() for e in employees]


def employee_api(pk):
    """Return JSON of a sinlge employee identified by pk from the database"""
    employee = db_session.get(Employee, pk)
    return employee.to_dict()
