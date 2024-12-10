from flask import render_template, request, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash
from flask_login import login_user, login_required, logout_user

from application import app, db, login_manager
from application.models import Company, Test, Question, Option
from application.forms import RegisterForm, LoginForm, TestForm, QuestionForm, OptionForm
from application.db_operations import insert_in_db, get_all_companies

from sqlalchemy import text

@login_manager.user_loader #here
def load_user(user_id):
    return Company.query.get(int(user_id))    

@app.route("/", methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = Company.query.filter_by(work_email=form.work_email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Logged in successfully.', 'success')
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('dashboard_test'))
            else :
                flash('Login unsuccessful. Please check your <b>Work Email</b> and <b>Password</b>', 'danger')
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
            new_company = Company(
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
            return redirect(url_for('login'))
        
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


@app.route("/dashboard-test")
@login_required
def dashboard_test():
    try:
        companies = get_all_companies()
    except Exception as e:
        flash(f"An error occurred while fetching data: {str(e)}", "danger")
        return render_template("dashboard_test.html")
    return render_template("dashboard_test.html", companies=companies)

@app.route("/test-making", methods=["GET", "POST"])
@login_required
def test_making():
    user = Company.query.filter_by(id=session["_user_id"]).first()

    test_form = TestForm()
    question_form = QuestionForm()
    option_form = OptionForm()

    if request.method == "GET":
            return render_template("test_making.html", user=user, test_form=test_form, question_form=question_form, option_form=option_form)

    elif request.method == "POST":
        if not test_form.validate_on_submit() or not question_form.validate_on_submit() or not option_form.validate_on_submit():
            return render_template("test_making.html", user=user, test_form=test_form, question_form=question_form, option_form=option_form)
        
        new_test = Test(
            company_id = user.id,
            name = test_form.name.data,
            duration = test_form.duration.data,
            instructions = test_form.instructions.data,
            category = test_form.category.data,
            num_of_questions = test_form.num_of_questions.data,
            total_marks = test_form.total_marks.data
        )
        print("new_test: ", new_test.to_dict())

        try:
            insert_in_db(new_test)
        except Exception as e:
            flash(f"An error occurred while creating the test: {str(e)}", "danger")
            return redirect(url_for("test_making"))
        

        new_question = Question(
            test_id = new_test.id,
            question = question_form.question.data,
            type = question_form.type.data,
            marks = question_form.marks.data
        )
        print("new_question: ", new_question.to_dict())

        try:
            insert_in_db(new_question)
        except Exception as e:
            flash(f"An error occurred while creating the question: {str(e)}", "danger")
            return redirect(url_for("test_making"))
        

        options = request.form.getlist('option')
        is_corrects = request.form.getlist('is_correct')

        # Combine options and their corresponding is_correct values
        combined = list(zip(options, is_corrects))

        # Retrieve all options
        for option_text, is_correct_val  in combined:
            new_option = Option(
                question_id = new_question.id,
                test_id = new_test.id,
                option = option_text,
                is_correct = True if is_correct_val == 'y' else False
            )
            print("new_option: ", new_option.to_dict())

            try:
                insert_in_db(new_option)
            except Exception as e:
                flash(f"An error occurred while creating the option: {str(e)}", "danger")
                return redirect(url_for("test_making"))
        
        flash("Test has been successfully created!", "success")
        return redirect(url_for("test_making"))
    
    else:
        return render_template("test_making.html", user=user, test_form=test_form, question_form=question_form, option_form=option_form)
    

@app.route("/test-db-connection")
def test_db_connection():
    try:
        # Attempt to query the database
        db.session.execute(text('SELECT 1'))
        return "Database connection is working.", 200
    except Exception as e:
        return f"Database connection failed: {str(e)}", 500