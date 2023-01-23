from flask import Blueprint, jsonify, request
from ..service.project_service import (
    findAll, 
    create, 
    findOneProject, 
    changeStateProject)

project = Blueprint("project", __name__)


@project.route("/", methods=["GET"])
def get_all_projects():
    try:
        return jsonify({"projects": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@project.route("/<id>", methods=["GET"])
def get_one_projects(id):
    try:
        return jsonify({"project": findOneProject(id)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404

"""
* AQUI PUEDE CREAR EL PROYECTO UN PROFESOR O UN ESTUDIANTE
* SI LO CREA EL PROFESOR EL STATE DEBE SER ON_HOLD (EN ESPERA)
* SI LO CREA UN ALUMNO EL STATE DEBE SER PROPOSAL (PROPUESTA)
* CAMBIA DE ON_HOLD A IN_PROCCESS CUANDO EL PROFESOR APRUEBE EL PROYECTO QUE EL ALUMNO PROPUSO
* CAMBIA FINISHED CUANDO EL PROYECTO SE CULMINO CON EXITO
"""
@project.route("/create", methods=["POST"])
def create_project():
    try:
        print("hola")
        data = request.get_json()
        return jsonify({"project": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 400


"""
* EL DOCENTE CAMBIA LOS ESTADOS DEL PROYECTO
* PUEDE CAMBIARLOS A IN_PROCESS Y FINISHED
"""
@project.route("/start_project/<id>/<state>")
def change_state_project(id, state):
    try:
        return jsonify({"msg": changeStateProject(id, state)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


# @project.route('/propose_project/<state>', methods=['POST'])
# def propose_project(state):
#     try:
#         return jsonify({'proposal':})
#     except Exception as error:
#         return jsonify({'msg':error.args}), 400
