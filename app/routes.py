from flask import Flask,render_template, request
from app.models import get_projects_by_score, Project
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app, db

@app.route('/')
@app.route('/index')
def hello_world():
   projects = get_projects_by_score()
   print(projects)
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

@app.route('/projects', methods=['GET', 'POST'])
def projects():

   if request.method == "POST":
      title = request.form['title']
      print(title)
      description = request.form['description']
      project = Project(creator_id = 1, title=title, description=description, score=0, total_funding=0)
      db.session.add(project)
      db.session.commit()
      #return request.form['title']

   projects = get_projects_by_score()
   return render_template('projects.html', title='My Projects', projects=projects)

@app.route('/investments')
def project():
   projects = [
      {'name': 'Help Frogs', 'score': 50},
      {'name': 'Help Frongs', 'score': 50}
   ]
   return render_template('investments.html', title='My Investments', projects=projects)

if __name__ == '__main__':
    app.run(debug = True)
