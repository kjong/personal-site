from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    name_input = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Generate')
