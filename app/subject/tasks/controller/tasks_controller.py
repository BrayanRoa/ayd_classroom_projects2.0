from flask import Blueprint, jsonify, request, g
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from ....auth.user.user_dto import UserDtO
from ..service.tasks_service import (
  findAll, 
  findByGroupId, 
  deleteTask, 
  createTask,
  update)

task = Blueprint("task", __name__)

@task.before_request
def before_request():
    if verify_jwt_in_request():
        token = get_jwt()
        user_info = UserDtO(institutional_mail=token["sub"], role=token["role"])
        g.user_info = user_info.__str__()
        if g.user_info["role"] != "docente":
            return (
                jsonify({"unauthorized": "you don't have the necessary permissions"}),
                401,
            )

@task.route("/", methods=["GET"])
def get_all_task():
    try:
        return jsonify({"msg": findAll()}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@task.route("/task_of_group/<group>", methods=["GET"])
def task_of_group(group):
    """Get all task of one group ✅
    ---
    tags:
      - Tasks

    parameters:
      - name: group
        in: path
        required: true
        description: Identifier group

    definitions:
       GroupTask:
        type: object
        properties:
          id:
            type: string
          name:
            type: string
          description:
            type: string
          create_at:
            type: string
          expired_date:
            type: string

    responses:
      200:
        description: Get all task of one group
        schema:
          $ref: '#/definitions/GroupTask'
    """
    try:
        return jsonify({"msg": findByGroupId(group)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@task.route("/delete_task/<id>", methods=["DELETE"])
def delete_task(id):
    """Delete one task by id ✅
    ---
    tags:
      - Tasks

    parameters:
      - name: id
        in: path
        required: true
        description: Identifier task

    definitions:
       DeleteTask:
        type: object
        properties:
          msg:
            type: string

    responses:
      200:
        description: Delete one task
        schema:
          $ref: '#/definitions/DeleteTask'
    """
    try:
        return jsonify({"msg": deleteTask(id)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@task.route("/create", methods=["POST"])
def create_task():
    """add a new task in group ✅
    ---
    tags:
      - Tasks

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/TaskInfo'

    definitions:
       TaskInfo:
        type: object
        properties:
          name:
            type: string
          description:
            type: string
          expired_date:
            type: string
            format: date
          group_id:
            type: number

    responses:
      201:
        description: a new task
        schema:
          $ref: '#/definitions/TaskInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"msg": createTask(data)}), 201
    except Exception as error:
        return jsonify({"msg": error.args}), 404


@task.route('/update/<id>', methods=['PATCH'])
def update_task(id):
    """update task of group ✅
    ---
    tags:
      - Tasks
      
    description:
      fields that will not be updated should not be sent

    parameters:
      - name: id
        in: path
        required: true
        description: identifier group
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/TaskUpdate'

    definitions:
       TaskUpdate:
        type: object
        properties:
          name:
            type: string
          description:
            type: string
          expired_date:
            type: string
            format: date
          group_id:
            type: number

    responses:
      200:
        description: task updated
        schema:
          $ref: '#/definitions/TaskUpdate'
    """
    try:
        data = request.get_json()
        return jsonify({"msg": update(id, data)}), 200
    except Exception as error:
        return jsonify({"msg": error.args}), 404