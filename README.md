## Classroom Projects UFPS - 🧑‍🎓

<p align="center">
  <a target="blank"><img src="https://ingsistemas.cloud.ufps.edu.co/rsc/img/logo_vertical_ingsistemas_ht180.png" width="300" alt="python-flask-postgresql-docker" /></a>
</p>

1. Clone the repository
2. Create the virtual environment 

```
python3 -m virtualenv venv
```
3. install the necessary libraries that are in the archive ```requirements.txt```

```
pip install -r requirements.txt
```

4. enter the following commands

```
export FLASK_APP=entrypoint
```

```
export FLASK_DEBUG=1
```

* Steps required to create the tables 
```
flask shell
``` 

```
from app.db import db
```

```
db.create_all()
```

* Launch the app 🚀
```
flask run
```

5. You can access the api documentation here:

```
http:localhost:5000/apidocs
```
# Stack

* Flask 
* PostgreSql 
* Docker

<p align="center">
  <a target="blank"><img src="https://mukulrathi.com/static/9340fcb15b4c44184a11848ce18fb4c8/8326d/docker-flask-postgres.png" width="300" alt="python-flask-postgresql-docker" /></a>
</p>