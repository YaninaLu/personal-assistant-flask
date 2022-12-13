from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


app = Flask(__name__)
app.debug = True
app.config.from_object(config.Config)
db = SQLAlchemy()
db.init_app(app)
migration = Migrate(app, db)

from src.entity import models
from src import routes
