import os
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


# check whether tag was used before!

    
#    def __init__(self, *args, **kwargs):
#        FlaskForm.__init__(self, *args, **kwargs)
#        self.user = None



    def validate(self):
        print( "VALIDATE")
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        if self.email == None or self.email.data == '':
            user = "anonymous"
        else:
            user = self.email.data
        print( "validate: " + user )
        ##print( "path: " + os.getcwd())
        for root, dirs, files in os.walk( "data/" ):
            #print( root )
            if root == "data/" or root[5:] != user: continue
            
            for name in dirs:
                #print( root + '  <' + name + '> tag: <' + self.tag.data + '>'  )
                if self.tag.data == name:

                    #print ("TROUBLE CASE")
                    self.tag.errors.append( 'Choose different tag. Tag was previously used by user ' + user )
                    return False

        return True
