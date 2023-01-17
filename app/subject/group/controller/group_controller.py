from flask import Blueprint, jsonify
from ..service.group_service import findAll

group = Blueprint('group', __name__)



@group.route('/', methods=['GET'])
def get_all_groups():
    try:
        return jsonify({'groups':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404

