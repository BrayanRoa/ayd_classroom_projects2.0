from flask import Blueprint, jsonify, request
from ..service.project_person_service import findAll, registerPersonInProject, withdrawFromProject

project_person = Blueprint('project_person', __name__)


@project_person.route('/', methods=['GET'])
def get_all_project_person():
    try:
        return jsonify({'project_person':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    

@project_person.route('/register_person_in_project', methods=['POST'])
def register_person_in_project():
    """Register person in project
    ---
    tags:
      - Projects
      
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/RegisterPersonProject'

    definitions:
       RegisterPersonProject:
        type: object
        properties:
          institutional_mail:
            type: string
          project_id:
            type: number

    responses:
      201:
        description: register person in project
        schema:
          $ref: '#/definitions/RegisterPersonProject'
    """
    try:
        data = request.get_json()
        return jsonify({'project_person':registerPersonInProject(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 404 
    

@project_person.route('/withdraw_person_of_project', methods=['DELETE'])
def withdrawPersonOfProject():
    """abandon project
    ---
    tags:
      - Projects
      
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/RegisterPersonProject'

    definitions:
       RegisterPersonProject:
        type: object
        properties:
          institutional_mail:
            type: string
          project_id:
            type: number

    responses:
      200:
        description: abandon project
        schema:
          $ref: '#/definitions/RegisterPersonProject'
    """
    try:
        data = request.get_json()
        return jsonify({'msg':withdrawFromProject(data)}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404 