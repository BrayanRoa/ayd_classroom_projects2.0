from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt, jwt_required
from ..service.group_service import findAll, findPersonOfGroup, create
from ....auth.user.user_dto import UserDtO

group = Blueprint("group", __name__)


@group.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()


@group.route("/", methods=["GET"])
def get_all_groups():
    try:
        return jsonify({"groups": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@group.route("/<group>")
@jwt_required()
def get_all_person_of_subject(group):
    """Get all people in a group ✅
    ---
    tags:
      - Group

    parameters:
      - name: group
        in: path
        type: number
        required: true
        description: Identifier group

    definitions:
       ListPersonOfGroup:
        type: object
        properties:
          id:
            type: number
          name:
            type: string
          number_of_students:
            type: number
          person_group:
            type: object
            properties:
              cancelled:
                type: boolean
              state:
                type: string
              person:
                type: object
                properties:
                  code:
                    type: string
                  name:
                    type: string
                  lastnames:
                    type: string
                  institutional_mail:
                    type: string
          subject:
            type: object
            properties:
              code:
                type: string
              name:
                type: string
          subject_id:
            type: string


    responses:
      200:
        description: Get all people in a group
        schema:
          $ref: '#/definitions/ListPersonOfGroup'
    """
    try:
        return jsonify({"persons": findPersonOfGroup(group)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@group.route("/create", methods=["POST"])
@jwt_required()
def create_group():
    """add group to subject ✅
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
          number_of_students:
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
        if g.user_info["role"] != "docente":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )
        data = request.get_json()
        return jsonify({"group": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404
