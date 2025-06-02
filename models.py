from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}, Room {self.room_number}>"

    @staticmethod
    def add_student(name, email, age, room_number):
        """Safely add a new student to the database."""
        try:
            new_student = Student(
                name=name,
                email=email,
                age=int(age),
                room_number=room_number
            )
            db.session.add(new_student)
            db.session.commit()
            return f"✅ Successfully added {name}"
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            return f"❌ Error adding student: {e}"
