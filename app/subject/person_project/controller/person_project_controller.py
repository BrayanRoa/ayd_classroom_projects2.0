from flask import Blueprint, jsonify, request
from ..service.person_project_service import findAll, registerPersonInProject, withdrawFromProject

person_project = Blueprint('person_project', __name__)


@person_project.route('/', methods=['GET'])
def get_all_person_project():
    try:
        return jsonify({'person_project':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
# * HARIA FALTA VALIDAR QUE LA PERSONA ESTE REGISTRADA EN ESA GRUPO Y EN ESA MATERIA
@person_project.route('/register_person_in_project', methods=['POST'])
def register_person_in_project():
    """Register person in project 🛑🧑‍🔧
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
          person_id:
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
        return jsonify({'person_project':registerPersonInProject(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 404 
    

@person_project.route('/withdraw_person_of_project', methods=['DELETE'])
def withdrawPersonOfProject():
    """abandon project ✅
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
          person_id:
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