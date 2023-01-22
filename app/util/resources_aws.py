import boto3  # * ME PERMITE INTERACTUAR CON LOS SERVICIOS DE AWS

# from config import S3_BUCKET, S3_KEY, S3_SECRET
import os  # * ME PERMITE INTERACTUAR CON EL SO
from flask import session

# * OBTIENE EL NOMBRE DEL BUCKET DE S3 DONDE SE ALMACENARAR LOS ARCHIVOS
S3_BUCKET = os.getenv("AYD_S3_BUCKET", "ayd-project")

# * SE TOMA EL NOMBRE DEL USUARIO QUE ESTA REGISTRADO EN AWS, DE AQUI SE TOMAN EL "AWS_ACCESS_KEY_ID" Y EL "AWS_SECRET_ACCESS_KEY"
os.environ["AWS_PROFILE"] = "brayanroa" #! SOLO COLOQUE UN NOMBRE AL AZAR

# * SE ESPECIFICA LA REGION
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# * CONJUNTO DE EXTENSIONES PERMITIDAS
ALLOWED_PHOTO_EXTENSIONS = {"png", "jpg", "jpeg"}

"""
* es una función auxiliar, es decir, 
* es una función que se utiliza como 
* una herramienta para otras funciones en el código. 
* En este caso, se podría utilizar para
* obtener un recurso S3 en otras funciones de la aplicación.
"""
def _get_s3_resource():
    return boto3.resource("s3")


"""
* la última linea obtiene el bucket en el cual vamos a
* guardar los archivos, para poder hacer esta linea
* primero debemos llamar la funcion _get_s3_resource(), 
* justamente es lo que se hace en la primera linea 
* dentro del método
"""
def get_bucket():
    s3_resource = _get_s3_resource()
    if "bucket" in session:
        bucket = session["bucket"]
    else:
        bucket = S3_BUCKET

    return s3_resource.Bucket(bucket)


"""
* se encarga de obtener una lista de buckets 
* existentes en tu cuenta de S3
"""
def get_buckets_list():
    client = boto3.client("s3")
    return client.list_buckets().get("Buckets")


#* function to check file extension
def allowed_photo_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_PHOTO_EXTENSIONS
    )
