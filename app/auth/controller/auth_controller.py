from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
import datetime
from ...person.person.service.person_service import findOneByMail


auth = Blueprint("auth", __name__)


@auth.route("/login/<email>", methods=["POST"])
def login(email):
    """Login with institutional mail ✅
    ---
    tags:
      - Auth
      
    parameters:
      - name: email
        in: path
        type: string
        required: true
        description: identifier person

    definitions:
       loginInfo:
        type: object
        properties: 
          msg:
            type: string
         
    responses:
      200:
        description: access granted
        schema:
          $ref: '#/definitions/loginInfo'
    """
    try:
        person = findOneByMail(email)

        expires = datetime.timedelta(hours=3)
        additional_claims = {
            "role": person["role"]["name"],
        }

        access_token = create_access_token(
            identity=person["institutional_mail"],
            additional_claims=additional_claims,
            expires_delta=expires,
        )

        return jsonify({"access_token": access_token})
    except Exception as e:
        return jsonify({"msg": e.args}), 400
