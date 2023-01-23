from flask import Blueprint, jsonify, request
from ..service.project_service import findAll, create, findOneProject

project = Blueprint('project', __name__)


@project.route('/', methods=['GET'])
def get_all_projects():
    try:
        return jsonify({'projects':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    

@project.route('/<id>', methods=['GET'])
def get_one_projects(id):
    try:
        return jsonify({'project':findOneProject(id)}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    

@project.route('/create', methods=['POST'])
def create_project():
    try:
        print('hola')
        data = request.get_json()
        return jsonify({'project':create(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 400
    

# @project.route('/propose_project/<state>', methods=['POST'])
# def propose_project(state):
#     try:
#         return jsonify({'proposal':})        
#     except Exception as error:
#         return jsonify({'msg':error.args}), 400
