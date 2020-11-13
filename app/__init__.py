from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .routes import main, package
from .models import db

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main.bp)
app.register_blueprint(package.bp)
db.init_app(app)
migrate = Migrate(app, db)
