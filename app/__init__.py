from flask import Flask
from app.routes.scores import bp as scores_bp
import os

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.register_blueprint(scores_bp)
    return app
