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


#    def __init__(self, *args, **kwargs):
#        FlaskForm.__init__(self, *args, **kwargs)
#        self.user = None
#
#    def validate(self):
#        rv = FlaskForm.validate(self)
#        if not rv:
#            return False
#
#        user = User.query.filter_by(
#            username=self.username.data).first()
#        if user is None:
#            self.username.errors.append('Unknown username')
#            return False
#
#        if not user.check_password(self.password.data):
#            self.password.errors.append('Invalid password')
#            return False
#      
#
#    self.user = user
#    return True
