from flask_cors import CORS

def configure_cors(app):
    CORS(app, resources={r"/*": {"origins": "*"}})