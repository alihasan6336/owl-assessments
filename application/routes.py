from flask import render_template, request, flash, redirect
from werkzeug.security import generate_password_hash # Is this optimal?

from application import app, db
from application.models import Companies
from application.forms import RegisterForm, LoginForm
from application.db_operations import insert_in_db, get_all_companies

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            
            new_company = Companies(
                first_name     = form.first_name.data,
                last_name      = form.last_name.data,
                work_email     = form.work_email.data,
                department     = form.department.data,
                phone_number   = form.phone_number.data,
                country_code   = form.country_code.data,
                gender         = form.gender.data,
                date_of_birth  = form.date_of_birth.data,
                company_name   = form.company_name.data,
                country        = form.country.data,
                state          = form.state.data,
                city           = form.city.data,
                postal_code    = form.postal_code.data,
                street_address = form.street_address.data,
                building       = form.building.data,
                floor          = form.floor.data,
                apartment      = form.apartment.data,
                address_2      = form.address_2.data,
                passhash       = generate_password_hash(form.password.data) # Is this optimal?
            )

            try:
                insert_in_db(new_company)
            except Exception as e:
                flash(f"An error occurred while registering: {str(e)}", "danger")
                return redirect("/register") # Or url_for? 

            flash("You have successfully registered!", "success")
            return redirect("/register")
            # return {"form": form.data}, 200
        else:
            for field, errors in form.errors.items(): # Explian this.
                for error in errors:
                    flash(f"{error}", "danger")
            # return {"errors": form.errors}, 400
    return render_template("register.html", form=form)

# @app.route("/test_db_connection")
# def test_db():
#     try:
#         results = db.session.query(db.text("1")).from_statement(db.text("SELECT 1")).all()
#         result = [row[0] for row in results]
#         return {'result': result}, 200
#     except Exception as e:
#         return {'error': str(e)}, 500
    

@app.route("/dashboard_test")
def dashboard_test():
    try:
        companies = get_all_companies()
    except Exception as e:
        flash(f"An error occurred while fetching data: {str(e)}", "danger")
        return render_template("dashboard_test.html")
    return render_template("dashboard_test.html", companies=companies)
    # return {"companies": [company.to_dict() for company in companies]}, 200