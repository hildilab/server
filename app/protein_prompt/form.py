from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators, ValidationError

class SequenceForm( FlaskForm ):
    sequence = StringField('Drop your sequence here', validators=[validators.DataRequired("fasta or plain")])
    tag = StringField('Tag your job, so you can find results', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional)' , validators=[validators.Email("Not recognized as email")])
    submit = SubmitField('Submit')

