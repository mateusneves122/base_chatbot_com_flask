from flask import Flask
from .botwp.bot import bp_bots

def create_app():
    app = Flask(__name__);
    app.register_blueprint(bp_bots);
    return app;