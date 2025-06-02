from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student
from config import Config
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')

        # Check if the email already exists
        existing_student = Student.query.filter_by(email=email).first()
        if existing_student:
            flash("❌ Email already exists! Please use a different one.", "error")
            return redirect(url_for('register'))

        # Register new student
        name = request.form.get('name')
        age = request.form.get('age')
        room_number = request.form.get('room_number')

        new_student = Student(name=name, email=email, age=int(age), room_number=room_number)

        try:
            db.session.add(new_student)
            db.session.commit()
            flash("✅ Registration Successful!", "success")  # Message now appears properly
            return redirect(url_for('home'))
        except IntegrityError:
            db.session.rollback()
            flash("❌ There was an error processing your request!", "error")
            return redirect(url_for('register'))

    return render_template('register.html')
