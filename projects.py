from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

POSTGRES_URL="127.0.0.1:5432"
POSTGRES_USER="dmoney"
POSTGRES_PW="password"
POSTGRES_DB="test"

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,
        pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create our database model
class Projects(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    score = db.Column(db.Integer)





@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')
