from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt, jwt_required
from app.person.person.service.person_service import (
    findAll,
    findOneByMail,
    create,
    findTeachers,
    registerInCourse,
    updateImage,
)
from ....auth.user.user_dto import UserDtO
from ....util.resource_cloudinary import allowed_photo_file, ALLOWED_PHOTO_EXTENSIONS
import os

person = Blueprint("person", __name__)


@person.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()


@person.route("/", methods=["GET"])
@jwt_required()
def get_all_persons():
    """Returning list all persons ✅
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
        if g.user_info["role"] != "docente":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )
        return jsonify({"persons": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/<term>", methods=["GET"])
def get_person_by_mail(term):
    """get person by institutional mail or code ✅
    ---
    tags:
      - Person

    parameters:
      - name: term
        in: path
        type: string
        required: true
        description: institutional mail or code

    definitions:
       LookPerson:
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
          person_group:
            type: object
            properties:
              cancelled:
                type: boolean
              state:
                type: string
              group:
                type: object
                properties:
                  id:
                    type: number
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
        description: One person by institutional_mail or code
        schema:
          $ref: '#/definitions/LookPerson'
    """
    try:
        return jsonify({"person": findOneByMail(term)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/get_teachers", methods=["GET"])
def get_all_teachers():
    """Returning list all teacher ✅
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
        if g.user_info["role"] != "docente":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )
        return jsonify({"teachers": findTeachers()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@person.route("/create", methods=["POST"])
def create_person():
    """add a new person ✅
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
    """Register person in group ✅
    ---
    tags:
      - Person

    description:
      when a person is registered, the state must be 'in_process'

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/PersonGroupInfo'

    definitions:
       PersonGroupInfo:
        type: object
        properties:
          person_id:
            type: string
          subject_id:
            type: string
          group_id:
            type: number
          state:
            type: string

    responses:
      201:
        description: Register person in group
        schema:
          $ref: '#/definitions/PersonGroupInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"registration": registerInCourse(data)})
    except Exception as error:
        return jsonify({"msg": error.args})


@person.route("/upload_image/<mail>", methods=["PATCH"])
@jwt_required()
def upload_image(mail):
    """Update a person's profile picture ✅
    ---
    tags:
      - Person
    parameters:
      - name: mail
        in: path
        description: Identifier person
        required: true
        type: string
      - name: file
        in: formData
        description: The uploaded file data
        required: true
        type: file

    responses:
      200:
        description: A File
    """
    try:
        if "file" not in request.files:
            return jsonify({"msg": "there is no file in the request"}), 400
        my_file = request.files["file"]
        if not allowed_photo_file(my_file.filename):
            return jsonify({"msg": f"invalid image extension - allowed: {ALLOWED_PHOTO_EXTENSIONS}"})
        return jsonify({"URL": updateImage(my_file, mail)})
    except Exception as error:
        return jsonify({"msg": error.args})


# * UPDATE PERSON