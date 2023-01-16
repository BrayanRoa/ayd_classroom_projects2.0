## SKELETON TO START PROJECT IN PYTHON

<p align="center">
  <a target="blank"><img src="https://mukulrathi.com/static/9340fcb15b4c44184a11848ce18fb4c8/8326d/docker-flask-postgres.png" width="300" alt="python-flask-postgresql-docker" /></a>
</p>

1. Clone the repository
2. Create the virtual environment __python3 -m virtualenv venv__
3. install the necessary libraries that are in the archive ```requirements.txt```

* __pip install -r requirements.txt__

4. enter the following commands

* __export FLASK_APP=entrypoint__
* __export FLASK_DEBUG=1__
* __flask shell__ --> Steps required to create the tables
  * __from app.db import db__
  * __db.create_all()__
* __flask run__

# Stack

* Flask 
* PostgreSql 
* Docker