from flask import Response

from models.user_model import *
from app import vuln

def populate_db():
    db.drop_all()
    db.create_all()
    User.init_db_users()
    response_text = '{ "message": "Database populated." }'
    response = Response(response_text, 200, mimetype='application/json')
    return response

def basic():
    response_text = '{ "message": "VAPI the Vulnerable API", "help": "VAPI is a vulnerable on purpose API. ' \
                    'It can be used for learning/teaching purposes. You have permission to do whatever you want to this API.", "vulnerable":' + "{}".format(vuln) + "}"
    response = Response(response_text, 200, mimetype='application/json')
    return response
