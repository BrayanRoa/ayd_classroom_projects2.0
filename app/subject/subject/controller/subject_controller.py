from flask import Blueprint, jsonify, request
from ..service.subject_service import findAll, create, findOneByCode


subject = Blueprint("subject", __name__)


@subject.route("/", methods=["GET"])
def get_all_subject():
    """returns the list of all subjects with their groups ✅
    ---
    tags:
      - Subject
      
    definitions:
       Subject:
        type: object
        properties:
          code:
            type: string
          name:
            type: string  
          group:
            type: object
            properties:
              id:
                type: number
              name:
                type: string
              number_of_students:
                type: number            
          
    responses:
      200:
        description: A list of Subject
        schema:
          $ref: '#/definitions/Subject'
    """
    try:
        return jsonify({"subjects": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@subject.route("/<code>", methods=["GET"])
def get_one_subject(code):
    """Search for a subject by code ✅
    ---
    tags:
      - Subject
      
    parameters:
      - name: code
        in: path
        type: string
        required: true
        description: Identifier subject

    definitions:
       Subject:
        type: object
        properties:
          code:
            type: string
          name:
            type: string  
          group:
            type: object
            properties:
              id:
                type: number
              name:
                type: string
              number_of_students:
                type: number 

    responses:
      200:
        description: One subject by code
        schema:
          $ref: '#/definitions/Subject'
    """
    try:
        return jsonify({"subject": findOneByCode(code)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@subject.route("/create", methods=["POST"])
def create_subject():
    """add a new subject ✅
    ---
    tags:
      - Subject

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/SubjectInfo'
          
    definitions:
       SubjectInfo:
        type: object
        properties:
          code:
            type: string
          name:
            type: string
          
    responses:
      201:
        description: a new subject
        schema:
          $ref: '#/definitions/SubjectInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"subject": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404
      
      
#* TODO: UPDATE SUBJECT
