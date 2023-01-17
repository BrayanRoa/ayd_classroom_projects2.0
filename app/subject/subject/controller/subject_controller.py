from flask import Blueprint, jsonify
from ..service.subject_service import findAll


subject = Blueprint('subject', __name__)


@subject.route('/', methods=['GET'])
def get_all_subject():
    try:
        return jsonify({'subjects':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404