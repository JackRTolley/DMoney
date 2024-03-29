from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Project

'''class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')'''


class ProjectForm(FlaskForm):
    name = StringField('Project Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Enter Project')

    def validate_name(self, name):
        title = Project.query.filter_by(title=name.data).first()
        if title is not None:
            raise ValidationError('Please use a different project title!')
