
from flask import Blueprint, jsonify, request
from ..service.advance_service import createAdvance

advance = Blueprint('advance', __name__)


@advance.route('/create', methods=['POST'])
def create():
    try:
        data = request.get_json()
        return jsonify({"msg":createAdvance(data)}), 201
    except Exception as error:
        return jsonify({"msg":error.args}), 400