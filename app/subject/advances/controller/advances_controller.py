
from flask import Blueprint, jsonify, request
from ..service.advance_service import createAdvance, findOneById, uploadFile

advance = Blueprint('advance', __name__)


@advance.route('/create', methods=['POST'])
def create():
    """add a new advance ✅
    ---
    tags:
      - Advances

    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/AdvanceInfo'
          
    definitions:
       AdvanceInfo:
        type: object
        properties:
          name:
            type: string
          description:
            type: string
          state:
            type: boolean
          delivery_date:
            type: string
            format: date
          project_id:
            type: number
          
    responses:
      201:
        description: advance added successfully
        schema:
          $ref: '#/definitions/AdvanceInfo'
    """
    try:
        data = request.get_json()
        return jsonify({"msg":createAdvance(data)}), 201
    except Exception as error:
        return jsonify({"msg":error.args}), 400
    

@advance.route('/<id>', methods=['GET'])
def get_one_advance(id):
    """get advance by id ✅
    ---
    tags:
      - Advances

    parameters:
      - name: id
        in: path
        required: true
        description: identifier advance
          
    definitions:
       Advance:
        type: object
        properties:
          id:
            type: number
          name:
            type: string
          description:
            type: string
          state:
            type: boolean
          delivery_date:
            type: string
            format: date
          project_id:
            type: number
          link: 
            type: string
          project:
            type: object
            properties:
              name:
                type: string
          
    responses:
      200:
        description: advance found successfully
        schema:
          $ref: '#/definitions/Advance'
    """
    try:
        return jsonify({"msg":findOneById(id)}), 200
    except Exception as error:
        return jsonify({"msg":error.args}), 400
    
    
@advance.route('/upload_file/<id>', methods=['PATCH'])
def upload_file(id):
    """upload documents to the system ✅
    ---
    tags:
      - Advances
    parameters:
      - name: id
        in: path
        description: Identifier advance
        required: true
        type: number
      - name: file
        in: formData
        description: The uploaded file data
        required: true
        type: file
          
    responses:
      200:
        description: A File
    """
    try:
        if "file" not in request.files:
            return jsonify({"msg":"there is no file in the request"})
        my_file = request.files["file"]
        return jsonify({"URL":uploadFile(id, my_file)})
    except Exception as error:
        return jsonify({"msg":error.args}), 400