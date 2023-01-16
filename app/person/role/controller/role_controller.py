
from flask import Blueprint, jsonify
from app.person.role.service.role_service import get_all

role = Blueprint('role', __name__)


@role.route('/', methods=['GET'])
def get_all_roles():
    try:
        return jsonify({'roles':get_all()}), 200
    except Exception as error:
        return jsonify({'error':error.args}), 404