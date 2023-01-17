from flask import Blueprint, jsonify
from app.person.person.service.person_service import get_all

person = Blueprint('person', __name__)


@person.route('/', methods=['GET'])
def get_all_persons():
    try:
        return jsonify({'persons':get_all()}), 200
    except Exception as error:
        return jsonify({'error':error.args}), 404
    
@person.route('/get_person_by_mail', methods=['GET'])
def get_person_by_mail():
    return ''