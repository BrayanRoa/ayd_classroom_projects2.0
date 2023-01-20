from flask import Blueprint, jsonify, request
from ..service.subject_service import findAll, create, findOneByCode


subject = Blueprint("subject", __name__)


@subject.route("/", methods=["GET"])
def get_all_subject():
    try:
        return jsonify({"subjects": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@subject.route("/<code>/<group>", methods=["GET"])
def get_one_subject(code, group):
    try:
        return jsonify({"subject": findOneByCode(code, group)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@subject.route("/create", methods=["POST"])
def create_subject():
    try:
        data = request.get_json()
        return jsonify({"subject": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404
