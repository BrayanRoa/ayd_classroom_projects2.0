from flask import Blueprint, jsonify, request
from ..service.tasks_service import findAll, findByGroupId, deleteTask

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
    

@task.route('/delete_task/<id>', methods=['DELETE'])
def delete_task(id):
    """Delete one task by id
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
        return jsonify({'msg':deleteTask(id)}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404 
      
  
#* TODO: CREAR TAREA


#* TODO: ACTUALIZAR TAREA?