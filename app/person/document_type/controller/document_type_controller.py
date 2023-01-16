from flask import Blueprint, jsonify
from app.person.document_type.service.document_type_service import get_all


document_type = Blueprint('document_type', __name__)


@document_type.route('/', methods=['GET'])
def get_all_documents_type():
    try:
        return jsonify({'document_types':get_all}), 200
    except Exception as error:
        return jsonify({'error':error.args}), 404