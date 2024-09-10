from flask import render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash
from flask_login import login_user, login_required, logout_user

from application import app, db, login_manager
from application.models import Companies
from application.forms import RegisterForm, LoginForm
from application.db_operations import insert_in_db, get_all_companies

@login_manager.user_loader #here
def load_user(user_id):
    return Companies.query.get(int(user_id))    

@app.route("/", methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = Companies.query.filter_by(work_email=form.work_email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Logged in successfully.', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('dashboard_test'))
            else :
                flash('Login Unsuccessful. Please check your Work Email and Password', 'danger')
                return redirect(url_for('login'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{error}", "danger")
    return render_template('login.html', form=form)

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
                passhash       = generate_password_hash(form.password.data)
            )

            try:
                insert_in_db(new_company)
            except Exception as e:
                flash(f"An error occurred while registering: {str(e)}", "danger")
                return redirect(url_for('register'))

            flash("You have successfully registered!", "success")
            return redirect(url_for('register'))
        
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"{error}", "danger")
    return render_template("register.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))


@app.route("/dashboard_test")
@login_required
def dashboard_test():
    try:
        companies = get_all_companies()
    except Exception as e:
        flash(f"An error occurred while fetching data: {str(e)}", "danger")
        return render_template("dashboard_test.html")
    return render_template("dashboard_test.html", companies=companies)