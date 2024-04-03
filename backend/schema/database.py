from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Doctors Table
class DoctorsTable(db.Model):
	__tablename__ = "doctor_table"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	specialty = db.Column(db.String, nullable=False)
	zipcode = db.Column(db.Integer, nullable=False)
	rating = db.Column(db.Integer, nullable=False)
	experience = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f'<Doctor> {self.id} / {self.name} / {self.specialty} / {self.zipcode} / {self.rating} / {self.experience}'