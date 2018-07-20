import time, os, subprocess 
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify, current_app
from celery import Celery
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import SelectField, StringField, SubmitField, validators, ValidationError

from form import SequenceForm
from execute import Execute
import sequence_functions as sf


app = Flask( __name__ )
app.config['SECRET_KEY'] = 'topf-sekret'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

bootstrap = Bootstrap(app)

app.config['USER_DATA_DIR'] = os.environ.get('USER_DATA_DIR') # feed from environment variable


choice =  [('1','Human'),('2','Mammalian'),('3','Vertebrata'),('4','Metazoa')]

class RequestForm( FlaskForm):
    sequence = StringField('Drop your sequence here:', validators=[validators.DataRequired("fasta or plain")])
    tag = StringField('Tag your job, so you can find results:', validators=[validators.DataRequired("Required!")])
    email = StringField( 'Email (optional):' , validators=[validators.Email("Not recognized as email")])
    db = SelectField('Select database to scan your query against:', choices = choice )
    submit = SubmitField('Submit your query to the server')


def func_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]



@celery.task(bind=True)
def submit_and_check_status(self, email, tag, sequence, db):
    with app.app_context():
        print ( "now entered submit:" + current_app.name )
        pwd = os.getcwd();
        if email == '':
            email = "anonymous"
        else:
            email = sf.FixPath( email )

        sequence = sf.CleanSequence( sequence )
        tag = sf.FixPath(tag)

        user_dir = app.config['USER_DATA_DIR']

        os.chdir( user_dir )
        job_dir = email + "/" + tag

        if os.path.isdir( job_dir):
#            status_message = tag + " exists for user: " + email + ", you will be redirected to the form"
#            self.update_state(state='PROGRESS',
#                              meta={ 'status': status_message})
#            time.sleep( 10 )
#            return {'status':'..failed'}
            time.sleep(1)
        else:
            os.makedirs( job_dir )
        os.chdir( job_dir )
        with open( 'protein_prompt.txt','w') as f:
            f.write( "fake.fa 15 AABCDEABCDEBCDE 0.4 \n")
            f.write( "cake.fa 105 ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE 0.5 \n")
            f.write( "bake.fa 5 ABCDE 1.5 \n")
        #cmd = "tsp rf -seq " + sequence + " -db " + db + " -out protein_prompt.txt"
        #        jiddle_id = subprocess.check_output( cmd ).strip()

        #       cmd = "echo fake.fa 5 ABCDE 0.5 > protein_prompt.txt".split()
        #        subprocess.call( cmd )

        go = True
        while go:
            status = "running" # subprocess.check_output( ["ts", "-s", jiddle_id] ).strip()

            # better: != running and != pending..
            if status == "finished":
                go = False
                status += ", you will be redirected to the result section soonish..."

            self.update_state(state='PROGRESS',
                              meta={ 'status': status})

            time.sleep(5)
            go = False
        os.chdir( pwd)
    return {'status':'completed'}



def page_url( filename):
    return ( request.base_url + "/" + filename)



def WriteLines( path):
    mstr = ""
    styles=["width:20%","width:20%","width:40%;overflow:hidden","width:20%"]
    with open( path + "/protein_prompt.txt" ) as f:
        for l in f:
            c = l.split()
            if len(c) < 4: continue
            mstr += "<tr>\n";
            for t,col in zip( styles,c):
                mstr+= "<td style=\"" + t + "\"> " + col + "</td>\n"
            mstr += "</tr>\n"
    return mstr



@app.route( '/' , methods=['GET', 'POST'])
def index():
    print( func_name() + " go")

    form = RequestForm()
#    form = RequestForm(db='1')

    if request.method=='GET':

        form.email.data = session.get('email','')
        form.sequence.data = session.get('sequence','')
        form.tag.data = session.get('tag','')
        form.db.data = session.get('db','1')
        
        print( func_name() + " get")
        print( func_name() + " " + form.email.data)
        print( func_name() + " " + form.tag.data)
        print( func_name() + " " + form.sequence.data)
        print( func_name() + " " + form.db.data)
        
        return render_template( 'form.html', form=form)
    

    print( func_name() + " post ")
    if form.validate() == False:
        print( func_name() + " errors " )
        flash( 'errors in input (see detailed information above)')
        return render_template( 'form.html', form=form)
    

    #    email = request.form['email']
    session['email'] = form.email.data
    session['tag'] = form.tag.data
    session['sequence'] = form.sequence.data
    session['db'] = form.db.data
    
    print( func_name() + " redirect")
    print( func_name() + " " + session.get('email'))
    print( func_name() + " " + session.get('tag'))
    print( func_name() + " " + session.get('sequence'))
    print( func_name() + " " + session.get('db'))
    return redirect( url_for( 'index' ) )
    


 

@app.route('/submit', methods=['POST'])
def submittask():
    print( func_name() )
    email = request.form['email']
    session['email'] = email

    tag = request.form['tag']
    session['tag'] = tag
    
    sequence = request.form['sequence']
    session['sequence'] = sequence
    
    db = request.form['db']
    session['db'] = db
    print( func_name() + " " + email )
    print( func_name() + " " + tag )
    print( func_name() + " " + sequence )
    print( func_name() + " " + db )
    
    task = submit_and_check_status.apply_async( args=(email,tag,sequence,db))
#    task = submit_and_check_status.apply_async( kwargs={'email':email , 'tag':tag, 'sequence':sequence, 'db':db})
#    task = submit_and_check_status.apply_async()
    print( func_name() + " submit send to background, id: " + str( task.id))
    print( func_name() + " forward status location: " +  url_for('taskstatus', task_id=task.id))
    return jsonify({}), 202, {'Location': url_for('taskstatus', task_id=task.id)}



@app.route('/status/<task_id>')
def taskstatus(task_id):
    print( func_name() + " id: " + task_id)
    task = submit_and_check_status.AsyncResult(task_id)
    print( func_name() + " async result: " + task.state + " " + task.status )
    if task.state == 'PENDING':
        print( func_name() + " pending")
        response = {
            'state': task.state,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        print( func_name() + " running")        
        response = {
            'state': task.state,
            'status': task.info.get('status', '')
        }
    else:
        print( func_name() + " trouble")
        # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info)  # this is the exception raised
        }
    print( func_name() + " jsonify response")
    return jsonify(response)



@app.route( '/results/<job_id>')
@app.route( '/results/<user>/<job_id>')
def results( job_id, user="unknown"):
#    email = request.form.get['email']
#    tag = request.form.get['tag']
    user = sf.FixPath( user )
#    path = app.config['USER_DATA_DIR'] + "/" + user + "/" + job_id 
    path = "data/" + user + "/" + job_id 
    all_lines = WriteLines( path)
    return render_template( 'results.html', user=user, job_id=job_id, lines=all_lines,result_path=path )
    
@app.route( '/prompt_results')
def list_results():
    path = "data/"
    mstr = ""
    for root, dirs, files in os.walk( path ):
        if path == root: continue
        
        for name in dirs:
            root = root[ len(path):]
            root = root.replace('_','@',1)
            root = root.replace('_','.')
            # clean strings: emails, paths
            mstr += "<tr><td>" + root + "</td><td><a href=\"/results/" + root + "/" + name + "\">"  + name + "</a></td></tr>\n"
      
    return render_template( 'list_results.html', lines=mstr )
    
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run( debug=True)
