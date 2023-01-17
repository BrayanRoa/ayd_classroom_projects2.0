from dotenv import load_dotenv
load_dotenv('.env')

import os

USER=os.environ['DB_USER']
PASSWORD=os.environ['DB_PASSWORD']
HOST=os.environ['DB_HOST']
PORT=os.environ['DB_PORT']
DB=os.environ['DB_NAME']

SQLALCHEMY_DATABASE_URI=f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '089ddfc7-3a3a-44be-8855-fefe437de664987eb9a7-294c-4dec-9303-e0f9b7a0da6ee933fd28-5eba-48b5-818f-322d2c020552'
