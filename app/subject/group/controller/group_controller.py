from flask import Blueprint, jsonify
from ..service.group_service import findAll, findPersonOfSubject

group = Blueprint("group", __name__)


@group.route("/", methods=["GET"])
def get_all_groups():
    try:
        return jsonify({"groups": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@group.route("/<subject>/<group>")
def get_all_person_of_subject(subject, group):
    try:
        return jsonify({"persons": findPersonOfSubject(subject, group)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404
