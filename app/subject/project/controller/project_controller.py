from flask import Blueprint, jsonify
from ..service.project_service import findAll

project = Blueprint('project', __name__)


@project.route('/', methods=['GET'])
def get_all_projects():
    try:
        return jsonify({'projects':findAll()})
    except Exception as error:
        return jsonify({'msg':error.args})