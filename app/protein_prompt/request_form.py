import os, re
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms import validators, ValidationError

class SequenceForm( FlaskForm ):
    sequence = StringField('Drop your sequence here', validators=[validators.DataRequired("fasta or plain")])
    tag = StringField('Tag your job, so you can find results', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional)' , validators=[validators.Email("Not recognized as email")])
    submit = SubmitField('Submit')

    
def IsEmail( email):
    if re.search( r'[,<>;\'\"\/?|\]\}\{\[=\+)(*&^%$#!~]', email , re.M|re.I):
        return False
    if not re.match( r"[^@]+@[^@]+\.[^@]+", email ):
        return False
#    jid = email.find( '@')
#    if jid < 0:
#        return False
#    if email[jid+2:].count('.') == 0:
#        return False
    return True



lyst = list("GPAVLIMCFYWHKRQNEDST")


def IsAA( word):
    for a in word:
        if a not in lyst:
            #print( "no aa seq")
            return False
    return True


choice =  [('1','Human'),('2','Mammalian'),('3','Vertebrata'),('4','Metazoa')]

class RequestForm( FlaskForm):
    sequence = StringField('Drop your sequence here:', validators=[validators.DataRequired("Enter plain sequence (without header)")])
    tag = StringField('Tag your job, so you can find results:', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional):' )
#    email = StringField( 'Email (optional):' , validators=[validators.Email("Not recognized as email")])
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

        self.sequence.data = self.sequence.data.strip().upper()
        self.tag.data = self.tag.data.strip()
        self.email.data = self.email.data.strip()
        
        if not IsAA( self.sequence.data ):
            self.sequence.errors.append( 'This does not look like a proper sequence. Only natural AA are accepted.')
            return False
        
        if self.email == None or self.email.data == '':
            self.email.data  = "anonymous"
        elif not IsEmail( self.email.data):
            self.email.errors.append( 'This does not look like a proper email.')
            return False

        print( "validate: " + self.email.data )
        ##print( "path: " + os.getcwd())
        for root, dirs, files in os.walk( "data/" ):
            #print( root )
            if root == "data/" or root[5:] != self.email.data: continue
            
            for name in dirs:
                print( root + '  <' + name + '> tag: <' + self.tag.data + '>'  )
                if self.tag.data == name:

                    print ("TROUBLE CASE")
                    self.tag.errors.append( 'Choose different tag. Tag was previously used by user ' + self.email.data )
                    return False

        return True
