from flask import Blueprint, jsonify, request
from ..service.project_service import findAll, create

project = Blueprint('project', __name__)


@project.route('/', methods=['GET'])
def get_all_projects():
    try:
        return jsonify({'projects':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
    
@project.route('/create', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        return jsonify({'project':create(data)})
    except Exception as error:
        return jsonify({'msg':error.args})