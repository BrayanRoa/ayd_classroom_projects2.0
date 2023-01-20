from flask import Blueprint, jsonify, request
from app.person.person.service.person_service import (
    findAll, 
    findOneByMail,
    create
    )

person = Blueprint("person", __name__)


@person.route("/", methods=["GET"])
def get_all_persons():
    try:
        return jsonify({"persons": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/<mail>", methods=["GET"])
def get_person_by_mail(mail):
    try:
        return jsonify({"person": findOneByMail(mail)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404
    
    
@person.route('/create', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        return jsonify({'person':create(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args})
