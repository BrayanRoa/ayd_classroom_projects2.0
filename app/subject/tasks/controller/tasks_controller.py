from flask import Blueprint, jsonify, request
from ..service.tasks_service import findAll, findByGroupId

task = Blueprint('task', __name__)


@task.route('/', methods=['GET'])
def get_all_task():
    try:
        return jsonify({'msg':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404 
    

@task.route('/task_of_group/<group>', methods=['GET'])
def task_of_group(group):
    """Get all task of one group
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
        return jsonify({'msg':findByGroupId(group)}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404 