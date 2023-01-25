from flask import Blueprint, jsonify, request
from app.person.document_type.service.document_type_service import findAll, create


document_type = Blueprint('document_type', __name__)


@document_type.route('/', methods=['GET'])
def get_all_documents_type():
    """Returning list all Document Types
    ---
    tags:
      - Document Type
      
    definitions:
       Document_type:
        type: object
        properties:
          id:
            type: number
          names:
            type: string  
          person:
            type: object
            properties:
              code:
                type: string
              institutional_mail:
                type: string
              names:
                type: string
              lastnames:
                type: string            
          
    responses:
      200:
        description: A list of document types
        schema:
          $ref: '#/definitions/Document_type'
    """
    try:
        return jsonify({'document_types':findAll()}), 200
    except Exception as error:
        return jsonify({'msg':error.args}), 404
    
    
@document_type.route('/create', methods=['POST'])
def create_document_type():
    """add a new document type
    ---
    tags:
      - Document Type

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/DocumentInfo'
    definitions:
       DocumentInfo:
        type: object
        properties:
          name:
            type: string

    responses:
      201:
        description: a new document type
        schema:
          $ref: '#/definitions/DocumentInfo'
    """
    try:
        data = request.get_json()
        return jsonify({'document_type':create(data)}), 201
    except Exception as error:
        return jsonify({'msg':error.args}), 404
        
        