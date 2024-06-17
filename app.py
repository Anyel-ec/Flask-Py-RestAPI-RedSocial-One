from flask import Flask
from app.controllers.user_controller import user_blueprint
from app.controllers.post_controller import post_blueprint
from app.controllers.category_controller import category_blueprint
from app.config.cors import configure_cors
from app.controllers.consumer_comment_controller import consumer_comment_blueprint


app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/api')
app.register_blueprint(post_blueprint, url_prefix='/api')
app.register_blueprint(category_blueprint, url_prefix='/api')
app.register_blueprint(consumer_comment_blueprint, url_prefix='/api')


configure_cors(app)

if __name__ == '__main__':
    app.run(debug=True)