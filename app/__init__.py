from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)



app = Flask(__name__)

from app import routes, projects
