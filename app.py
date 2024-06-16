from flask import Flask
from app.controller.user_controller import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
