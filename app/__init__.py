from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

bootstrap = Bootstrap()
csrf = CSRFProtect()
app = Flask(__name__)

from .views import page

def create_app(config):

    csrf.init_app(app)
    app.config.from_object(config)
    bootstrap.init_app(app)
    app.register_blueprint(page)
    return app