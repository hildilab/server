from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms import validators, ValidationError

class SequenceForm( FlaskForm ):
    sequence = StringField('Drop your sequence here', validators=[validators.DataRequired("fasta or plain")])
    tag = StringField('Tag your job, so you can find results', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional)' , validators=[validators.Email("Not recognized as email")])
    submit = SubmitField('Submit')


choice =  [('1','Human'),('2','Mammalian'),('3','Vertebrata'),('4','Metazoa')]

class RequestForm( FlaskForm):
    sequence = StringField('Drop your sequence here:', validators=[validators.DataRequired("fasta or plain")])
    tag = StringField('Tag your job, so you can find results:', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional):' , validators=[validators.Email("Not recognized as email")])
    db = SelectField('Select database to scan your query against:', choices = choice )
    submit = SubmitField('Submit your query to the server')

