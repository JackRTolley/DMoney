from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ProjectForm
from app.models import Project

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Home')

@app.route('/project', methods=['GET', 'POST'])
def projects():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.name.data, description=form.description.data, creator_id=1, score=10, total_funding=100)
        db.session.add(project)
        db.session.commit()
        flash('Project creation for project {}'.format(
            form.name.data))
        return redirect(url_for('index'))
    return render_template('form.html', title='Project Creator', form=form)
