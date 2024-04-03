from app import app, db
from flask import request, make_response, jsonify
from flask_cors import cross_origin
from schema.database import DoctorsTable

def get_all_doctors():
    doctors_query = DoctorsTable.query.all()

    doctors_list = [{
        'id': doctor.id,
        'name': doctor.name,
        'specialty': doctor.specialty,
        'zipcode': doctor.zipcode,
        'rating': doctor.rating,
        'experience': doctor.experience
    } for doctor in doctors_query]

    return doctors_list

@app.route("/retrieve-doctors", methods=['GET'])
@cross_origin()
def return_doctors():
    doctors = get_all_doctors()
    return jsonify(
        {
            "doctors": doctors
        }
    )

def get_similar_doctors(doc_id):
    specified_doctor = DoctorsTable.query.get(doc_id)
    doctors_query = DoctorsTable.query.filter(DoctorsTable.id != specified_doctor.id).order_by(
        DoctorsTable.specialty,  # Order by specialty
        DoctorsTable.zipcode,    # Then order by zipcode
        DoctorsTable.rating,     # Then order by rating
        DoctorsTable.experience  # Then order by experience
    ).all()

    doctors_list = [{
        'id': doctor.id,
        'name': doctor.name,
        'specialty': doctor.specialty,
        'zipcode': doctor.zipcode,
        'rating': doctor.rating,
        'experience': doctor.experience
    } for doctor in doctors_query]

    return doctors_list

@app.route("/retrieve-similar-doctors", methods=['GET'])
@cross_origin()
def return_similar_doctors():
    doctor_id = request.args.get('doctor_id')
    print(doctor_id)
    doctors = get_similar_doctors(doctor_id)
    return jsonify(
        {
            "doctors": doctors
        }
    )