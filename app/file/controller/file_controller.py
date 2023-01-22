from flask import Blueprint, request
# from flask_jwt_extended import jwt_required
from ..service.file_service import FileService as file_service

file = Blueprint("file_bp",__name__)

# @jwt_required()
@file.route('/<string:type>/<string:id>/photo/', methods=['POST'])
def upload_file(type,id):
    my_file = request.files['file']
    return file_service.upload_file(id, type, my_file)

