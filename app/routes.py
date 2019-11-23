from flask import render_template
from app import app
from app.forms import ProjectForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Home')

@app.route('/project')
def login():
    form = ProjectForm()
    return render_template('form.html', title='Project Creator', form=form)
