from flask import Blueprint, jsonify
from ..service.project_person_service import findAll

project_person = Blueprint('project_person', __name__)


@project_person.route('/', methods=['GET'])
def get_all_project_person():
    try:
        return jsonify({'project_person':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404