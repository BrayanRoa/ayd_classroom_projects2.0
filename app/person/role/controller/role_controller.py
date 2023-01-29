from flask import Blueprint, jsonify, request
from app.person.role.service.role_service import findAll, create

role = Blueprint("role", __name__)


@role.route("/", methods=["GET"])
def get_all_roles():
    """Returning list all Roles ✅
    ---
    tags:
      - Roles

    definitions:
       Roles:
        type: object
        properties:
          id:
            type: number
          names:
            type: string
          person:
            type: object
            properties:
              code:
                type: string
              institutional_mail:
                type: string
              names:
                type: string
              lastnames:
                type: string

    responses:
      200:
        description: A list of roles
        schema:
          $ref: '#/definitions/Roles'
    """
    try:
        return jsonify({"roles": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@role.route("/create", methods=["POST"])
def create_role():
    """add a new role ✅
    ---
    tags:
      - Roles

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/RoleInfo'
    definitions:
       RoleInfo:
        type: object
        properties:
          name:
            type: string

    responses:
      201:
        description: a new role
        schema:
          $ref: '#/definitions/RoleInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"role": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404
