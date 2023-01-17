from flask import Blueprint, jsonify
from app.person.person.service.person_service import findAll

person = Blueprint('person', __name__)


@person.route('/', methods=['GET'])
def get_all_persons():
    try:
        return jsonify({'persons':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
@person.route('/get_person_by_mail', methods=['GET'])
def get_person_by_mail():
    return ''