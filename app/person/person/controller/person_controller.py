from flask import Blueprint, jsonify, request
from app.person.person.service.person_service import (
    findAll,
    findOneByMail,
    create,
    findTeachers,
    registerInCourse,
    UpdateImage,
)
import os

person = Blueprint("person", __name__)


@person.route("/", methods=["GET"])
def get_all_persons():
    """Returning list all persons
    ---
    tags:
      - Person

    definitions:
       Person:
        type: object
        properties:
          institutional_mail:
            type: string
          names:
            type: string
          lastnames:
            type: string
          code:
            type: string
          img:
            type: string
          document_type:
            type: object
            properties:
              name:
                type: string
          groups:
            type: object
            properties:
              name: 
                type: string
              subject:
                type: object
                properties:
                  name: 
                    type: string
          role:
            type: object
            properties:
              name:
                type: string

    responses:
      200:
        description: A list of Person
        schema:
          $ref: '#/definitions/Person'
    """
    try:
        return jsonify({"persons": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/<mail>", methods=["GET"])
def get_person_by_mail(mail):
    """Returns a person by email
    ---
    tags:
      - Person
      
    parameters:
      - name: mail
        in: path
        type: string
        required: true
        description: Identifier person

    definitions:
       Person:
        type: object
        properties:
          institutional_mail:
            type: string
          names:
            type: string
          lastnames:
            type: string
          code:
            type: string
          img:
            type: string
          document_type:
            type: object
            properties:
              name:
                type: string
          groups:
            type: object
            properties:
              name: 
                type: string
              subject:
                type: object
                properties:
                  name: 
                    type: string
          role:
            type: object
            properties:
              name:
                type: string

    responses:
      200:
        description: A list of Person
        schema:
          $ref: '#/definitions/Person'
    """
    try:
        return jsonify({"person": findOneByMail(mail)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/get_teachers", methods=["GET"])
def get_all_teachers():
    """Returning list all teacher
    ---
    tags:
      - Person

    definitions:
       Person:
        type: object
        properties:
          institutional_mail:
            type: string
          names:
            type: string
          lastnames:
            type: string
          code:
            type: string
          img:
            type: string
          document_type:
            type: object
            properties:
              name:
                type: string
          groups:
            type: object
            properties:
              name: 
                type: string
              subject:
                type: object
                properties:
                  name: 
                    type: string
          role:
            type: object
            properties:
              name:
                type: string

    responses:
      200:
        description: A list of teacher
        schema:
          $ref: '#/definitions/Person'
    """
    try:
        return jsonify({"teachers": findTeachers()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/create", methods=["POST"])
def create_person():
    """add a new person
    ---
    tags:
      - Person

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/PersonInfo'
    definitions:
       PersonInfo:
        type: object
        properties:
          institutional_mail:
            type: string
          names:
            type: string
          lastnames:
            type: string
          code:
            type: string
          img:
            type: string
          document_type_id:
            type: number   
          role_id:
            type: number

    responses:
      201:
        description: a new person
        schema:
          $ref: '#/definitions/PersonInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"person": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args})


@person.route("/register_person_in_course", methods=["POST"])
def register_person_in_course():
    try:
        data = request.get_json()
        return jsonify({"registration": registerInCourse(data)})
    except Exception as error:
        return jsonify({"msg": error.args})


@person.route("/upload_image", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"msg": "there is no file in the request"}), 400
    my_file = request.files["file"]
    my_file.save(my_file.filename)
    return UpdateImage(my_file)


# @person.route('/excel_person', methods=['POST'])
# def excel_person():
#     if 'file' not in request.files:
#         return jsonify({'msg':'there is no file in the request'}), 400
#     excel = request.files['file']
#     excel.save(os.path.join('uploads', excel.filename))
#     createPersonExcel(excel.filename)
#     return 'ok'
