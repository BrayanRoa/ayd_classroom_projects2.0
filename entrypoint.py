import os
from app import create_app
from flask_jwt_extended import JWTManager

settings_module = os.getenv('APP_SETTINGS_MODULE')

if not settings_module:
    settings_module = os.environ.get('APP_SETTINGS_MODULE', 'config.development')
    
app = create_app(settings_module)
jwt = JWTManager(app)

@app.route('/input_test', methods=['GET'])
def test():
    return 'OK'