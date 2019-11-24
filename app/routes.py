from flask import Flask,render_template
from app.models import get_projects_by_score
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app, db



@app.route('/')
@app.route('/index')
def hello_world():
   projects = [
      {'name': 'Help Cats', 'score': 50},
      {'name': 'Help Dogs', 'score': 50}
   ]
   return render_template('index.html', title='Home', projects=projects)

@app.route('/account')
def account():
   transactions = [
      {'name': 'Help Cats', 'invested': 50, 'funded': 0.8, 'return': 0},
      {'name': 'Help Dogs', 'invested': 20, 'funded': 1, 'return': 2}
   ]
   data = {
      'investments': 100,
      'donations': 200,
      'returns': 10
   }
   return render_template('account.html', title='My Account', transactions=transactions, data=data)

@app.route('/projects')
def projects():
   projects = [
      {'name': 'Help Cats', 'score': 50},
      {'name': 'Help Dogs', 'score': 50}
   ]
   projects = get_projects_by_score()
   return render_template('projects.html', title='My Projects', projects=projects)

@app.route('/investments')
def project():
   projects = [
      {'name': 'Help Frogs', 'score': 50},
      {'name': 'Help Frongs', 'score': 50}
   ]
   return render_template('projects.html', title='My Projects', projects=projects)

if __name__ == '__main__':
    app.run(debug = True)
