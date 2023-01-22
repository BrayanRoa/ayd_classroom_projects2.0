from flask import jsonify
#from app.util.error_handling import ObjectNotFound, ObligatoryField
from app.util.resources_aws import get_bucket, allowed_photo_file
import os
from app.db import db

class FileService():

    """
    * Método que permite subir la photo de un tipo 
    * Los archivos permitidos son jpg, jpeg, png. Recibe el id cómo parámetro y el tipo
    * El nombre del archivo es el id del collaborator + la extensión original
    * El servicio devuelve el objecto Collaborator con el campo photo actualizado
    """
    def upload_file(self, id, type, file):

        url = ''
        
        #if collaborator_id is None:
        #        raise ObligatoryField('collaborator_id: Obligatory field')

        #collaborator = Collaborator.get_by_id(collaborator_id)
        
        #if collaborator is None:
        #    raise ObjectNotFound('Collaborator not exist')
        types = type.split(".")
        schema = types[0]
        model = types[1]
        field = types[2]
        # check whether the file extension is allowed (eg. png,jpeg,jpg)
        if file and allowed_photo_file(file.filename):
            my_bucket = get_bucket()
            extension = file.filename.split('.')[1]
            new_name = id + '.' + extension
            key = model + '/%s' % new_name
            my_bucket.Object(file.filename).put(Key=key, Body=file)
            
            # Generate the URL to get 'key-name' from 'bucket-name'
            url = "https://" + os.getenv('CRM_S3_BUCKET', 'hensall-ar-dev-files') + ".s3.amazonaws.com/" + key
            sql_clear = 'UPDATE '+schema+'.'+model+' SET '+field+' = \''+url+'\' where id = '+id
            db.session.execute(sql_clear)
            db.session.commit()

            resp = {
                'msg':'File Upload correctly',
                'url':url, 
                'code':200
            }
            return jsonify(resp), 200
        # if file extension not allowed
        else:
            resp = {
                'msg': 'File Type not accepted'
            }
            return jsonify(resp), 201
