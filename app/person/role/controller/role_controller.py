
from flask import Blueprint, jsonify
from app.person.role.service.role_service import findAll

role = Blueprint('role', __name__)

@role.route('/', methods=['GET'])
def get_all_roles():
    try:
        return jsonify({'roles':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404