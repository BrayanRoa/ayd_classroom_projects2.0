from flask import Blueprint, jsonify
from ..service.person_group_service import findAll, changeStateOfSubject

persons_groups = Blueprint("person_group", __name__)


@persons_groups.route("/", methods=["GET"])
def get_all_person_group():
    try:
        return jsonify({"person_group": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@persons_groups.route("/change_state_subject/<mail>/<group>/<state>", methods=["PATCH"])
def change_state_subject(mail, group, state):
    """Cancel or approve person group
    ---
    tags:
      - Person
      
    parameters:
      - name: mail
        in: path
        type: string
        required: true
        description: Identifier person

      - name: group
        in: path
        type: number
        required: true
        description: Identifier group

      - name: state
        in: path
        type: string
        required: true
        description: state group - (approve or cancel)
        
    definitions:
       SubjectGroup:
        type: object
        properties:
          state:
            type: string
    
    responses:
      200:
        description: Get all people in a group
        schema:
          $ref: '#/definitions/SubjectGroup'
    """
    try:
        return jsonify({"state": changeStateOfSubject(mail, group, state)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404