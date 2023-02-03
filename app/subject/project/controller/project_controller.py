from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from ....auth.user.user_dto import UserDtO
from ....util.resource_cloudinary import allowed_excel_file, ALLOWED_FILE_EXTENSIONS
from ..service.project_service import (
    findAll,
    create,
    findOneProject,
    changeStateProject,
    updateProject,
    registerExcelOfProjects,
)

project = Blueprint("project", __name__)


@project.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()


@project.route("/", methods=["GET"])
def get_all_projects():
    """Get all projects without persons ✅
    ---
    tags:
      - Projects

    definitions:
       Project:
        type: object
        properties:
          id:
            type: number
          name:
            type: string
          description:
            type: string
          active:
            type: boolean
          state:
            type: string
          group_id:
            type: number
          number_of_students:
            type: number
          full:
            type: boolean

    responses:
      200:
        description: list of all projects
        schema:
          $ref: '#/definitions/Project'
    """
    try:
        return jsonify({"projects": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@project.route("/<id>", methods=["GET"])
def get_one_projects(id):
    """Get one project with all people ✅
    ---
    tags:
      - Projects

    parameters:
      - name: id
        in: path
        type: number
        required: true
        description: Identifier project

    definitions:
       OneProject:
        type: object
        properties:
          id:
            type: number
          name:
            type: string
          description:
            type: string
          active:
            type: boolean
          state:
            type: string
          group_id:
            type: number
          number_of_students:
            type: number
          full:
            type: boolean
          persons:
            type: object
            properties:
              code:
                type: string
              names:
                type: string
              lastnames:
                type: string

    responses:
      200:
        description: one project with all people
        schema:
          $ref: '#/definitions/OneProject'
    """
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
    """add a new project ✅
    ---
    tags:
      - Projects

    description:
      allowed states --> on_hold or proposal

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/ProjectInfo'

    definitions:
       ProjectInfo:
        type: object
        properties:
          name:
            type: string
          description:
            type: string
          state:
            type: string
          group_id:
            type: number
          number_of_students:
            type: number

    responses:
      201:
        description: a new project
        schema:
          $ref: '#/definitions/ProjectInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"project": create(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 400


@project.route("/change_state_project/<id>/<state>")
def change_state_project(id, state):
    """change the status of a project ✅
    ---
    tags:
      - Projects

    description:
      allowed states --> in_process or finished

    parameters:
      - name: id
        in: path
        required: true
        type: number
        description: identifier project

      - name: state
        in: path
        required: true
        type: string
        description: state of project

    definitions:
       MsgProject:
        type: object
        properties:
          msg:
            type: string

    responses:
      200:
        description: change state of project
    """
    try:
        if g.user_info["role"] != "role":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )
        return jsonify({"msg": changeStateProject(id, state)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@project.route("/update_project/<id>", methods=["PATCH"])
def update_project(id):
    """update project ✅
    ---
    tags:
      - Projects

    description:
      fields that will not be updated should not be sent

    parameters:
      - name: id
        in: path
        required: true
        description: identifier group
      - name: body
        in: body
        schema:
          $ref: '#/definitions/ProjectUpdate'

    definitions:
       ProjectUpdate:
        type: object
        properties:
          name:
            type: string
          description:
            type: string
          number_of_students:
            type: number

    responses:
      200:
        description: project updated
        schema:
          $ref: '#/definitions/ProjectUpdate'
    """
    try:
        data = request.get_json()
        return jsonify({"msg": updateProject(id, data)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@project.route("/excel_projects", methods=["POST"])
def load_projects():
    """load excel from projects ✅
    ---
    tags:
      - Projects
    parameters:
      - name: file
        in: formData
        description: The uploaded file data
        required: true
        type: file

    responses:
      200:
        description: A File
    """
    try:
        if "file" not in request.files:
            return jsonify({"msg": "there is no file in the request"}), 400
        my_file = request.files["file"]
        if not allowed_excel_file(my_file.filename):
            return jsonify(
                {"msg": f"invalid file extension - allowed: {ALLOWED_FILE_EXTENSIONS}"}
            )
        return jsonify({"msg": registerExcelOfProjects(my_file)})
    except Exception as error:
        return jsonify({"msg": error.args}), 404
