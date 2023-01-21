from flask import Blueprint, jsonify, request
from app.person.document_type.service.document_type_service import findAll, create


document_type = Blueprint('document_type', __name__)


@document_type.route('/', methods=['GET'])
def get_all_documents_type():
    try:
        return jsonify({'document_types':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
    
@document_type.route('/create', methods=['POST'])
def create_document_type():
    try:
        data = request.get_json()
        return jsonify({'document_type':create(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 404
        
        