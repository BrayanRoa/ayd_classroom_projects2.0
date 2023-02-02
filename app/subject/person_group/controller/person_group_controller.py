from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt, jwt_required
from ..service.person_group_service import findAll, changeStateOfSubject
from ....auth.user.user_dto import UserDtO

persons_groups = Blueprint("person_group", __name__)



@persons_groups.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()

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