from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import boto3
import os

from dotenv import load_dotenv
load_dotenv('.env')

key_id=os.environ.get('AWS_ACCESS_KEY_ID')
secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')

ma = Marshmallow()
migrate = Migrate()

s3 = boto3.client(
    's3',
    aws_access_key_id=key_id,
    aws_secret_access_key=secret_access_key)