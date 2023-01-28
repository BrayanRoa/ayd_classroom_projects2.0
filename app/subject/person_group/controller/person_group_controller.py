from flask import Blueprint, jsonify, request
from ..service.person_group_service import findAll, changeStateOfSubject

persons_groups = Blueprint("person_group", __name__)


@persons_groups.route("/", methods=["GET"])
def get_all_person_group():
    try:
        return jsonify({"person_group": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@persons_groups.route("/change_state_subject", methods=["PATCH"])
def change_state_subject():
    """Cancel or approve person group ✅
    ---
    tags:
      - Person
        
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/PersonGroupUpdate'
          
    definitions:
       PersonGroupUpdate:
        type: object
        properties:
          person_id:
            type: string
          group_id: 
            type: number
          state:
            type: string
    
    responses:
      200:
        description: changed status successfully
        schema:
          $ref: '#/definitions/PersonGroupUpdate'
    """
    try:
        data = request.get_json()
        return jsonify({"state": changeStateOfSubject(data)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404