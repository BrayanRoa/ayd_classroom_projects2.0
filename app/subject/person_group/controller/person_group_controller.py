from flask import Blueprint, jsonify
from ..service.person_group_service import findAll

persons_groups = Blueprint('person_group', __name__)


@persons_groups.route('/', methods=['GET'])
def get_all_person_group():
    try:
        return jsonify({'person_group':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404