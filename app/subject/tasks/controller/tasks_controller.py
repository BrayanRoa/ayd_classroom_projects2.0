from flask import Blueprint, jsonify, request
from ..service.tasks_service import findAll

task = Blueprint('task', __name__)


@task.route('/', methods=['GET'])
def get_all_task():
    try:
        return jsonify({'msg':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404 
    