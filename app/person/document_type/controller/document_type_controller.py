from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from ....auth.user.user_dto import UserDtO
from app.person.document_type.service.document_type_service import (
    findAll,
    create,
    update,
)

document_type = Blueprint("document_type", __name__)


@document_type.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()
        if g.user_info["role"] != "docente":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )


@document_type.route("/", methods=["GET"])
def get_all_documents_type():
    """Get a list of all types of documents ✅
    ---
    tags:
      - Document Type

    definitions:
       Document_type:
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
        description: A list of document types
        schema:
          $ref: '#/definitions/Document_type'
    """
    try:
        return jsonify({"document_types": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@document_type.route("/create", methods=["POST"])
def create_document_type():
    """add a new document type ✅
    ---
    tags:
      - Document Type

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/DocumentInfo'
    definitions:
       DocumentInfo:
        type: object
        properties:
          name:
            type: string

    responses:
      201:
        description: a new document type
        schema:
          $ref: '#/definitions/DocumentInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"document_type": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@document_type.route("/<id>", methods=["PATCH"])
def update_document_type(id):
    """update document type ✅
    ---
    tags:
      - Document Type

    parameters:
      - name: id
        in: path
        required: true
        description: identifier document type

      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/updateDocument'

    definitions:
      updateDocument:
        type: object
        properties:
          name:
            type: string

    responses:
      200:
        description: document updated successfully
        schema:
          $ref: '#/definitions/updateDocument'
    """
    try:
        data = request.get_json()
        return jsonify({"msg": update(id, data)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404
