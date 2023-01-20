
from flask import Blueprint, jsonify, request
from app.person.role.service.role_service import findAll, create

role = Blueprint('role', __name__)

@role.route('/', methods=['GET'])
def get_all_roles():
    try:
        return jsonify({'roles':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
    
@role.route('/create', methods=['POST'])
def create_role():
    try:
        data = request.get_json()
        return jsonify({'role':create(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 404