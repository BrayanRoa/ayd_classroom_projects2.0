from flask import Blueprint, jsonify, request
from ..service.group_service import findAll, findPersonOfSubject, create

group = Blueprint("group", __name__)


@group.route("/", methods=["GET"])
def get_all_groups():
    try:
        return jsonify({"groups": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@group.route("/<subject>/<group>")
def get_all_person_of_subject(subject, group):
    """Get all people in a group
    ---
    tags:
      - Group
      
    parameters:
      - name: subject
        in: path
        type: string
        required: true
        description: Identifier subject

      - name: group
        in: path
        type: number
        required: true
        description: Identifier group
        
    definitions:
       SubjectGroup:
        type: object
        properties:
          id:
            type: number
          name:
            type: string
          number_of_students:
            type: number
          persons:
            type: object
            properties:
              code:
                type: string
              name:
                type: string  
              lastnames:
                type: string
          subject:
            type: string
          subject_id:
            type: string
    
    responses:
      200:
        description: Get all people in a group
        schema:
          $ref: '#/definitions/SubjectGroup'
    """
    try:
        return jsonify({"persons": findPersonOfSubject(subject, group)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@group.route("/create", methods=["POST"])
def create_group():
    """add group to subject
    ---
    tags:
      - Group

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/GroupInfo'
          
    definitions:
       GroupInfo:
        type: object
        properties:
          name:
            type: string
          number_of_persons:
            type: number
          subject_id:
            type: string
          
    responses:
      201:
        description: a new group in subject
        schema:
          $ref: '#/definitions/GroupInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"group": create(data)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404
