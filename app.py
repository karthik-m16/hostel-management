from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Student
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        room_number = request.form.get('room_number')

        new_student = Student(name=name, email=email, age=int(age), room_number=room_number)
        db.session.add(new_student)
        db.session.commit()
        flash("Registration Successful!", "success")
        return redirect(url_for('home'))

    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
