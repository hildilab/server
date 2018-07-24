import time, os, subprocess
import sqlite3 as sql

from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify, current_app
from celery import Celery
from flask_bootstrap import Bootstrap

import sequence_functions as sf
from request_form import RequestForm

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




@celery.task(bind=True)
def submit_and_check_status(self, email, tag, sequence, db):
    with app.app_context():
        print ( "now entered submit:" + current_app.name )
        pwd = os.getcwd();
        print( pwd )
        if email == '':
            email = "anonymous"
        else:
            email = sf.QuickFix( email )
        print( email)
        sequence = sf.CleanSequence( sequence )
        print (sequence)
        tag = sf.QuickFix(tag)
        print( tag)
        user_dir = app.config['USER_DATA_DIR']

        connector = sql.connect("jobs.db")
        cursor = connector.cursor()

        os.chdir( user_dir )
        job_dir = email + "/" + tag

        print( job_dir )
        if os.path.isdir( job_dir):
            print ( "dir exists")
            status = 'exists'
            self.update_state(state='PROGRESS',
                              meta={ 'status': status})
            time.sleep( 3 )
            return {'status':status}
        else:
            os.makedirs( job_dir )
        os.chdir( job_dir )
        with open( 'protein_prompt.txt','w') as f:
            f.write( "fake.fa 15 AABCDEABCDEBCDE 0.4 \n")
            f.write( "cake.fa 105 ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE 0.5 \n")
            f.write( "bake.fa 5 ABCDE 1.5 \n")
        #cmd = "tsp rf -seq " + sequence + " -db " + db + " -out protein_prompt.txt"
        cmd = "tsp sleep 20".split()
        jiddle_id = subprocess.check_output( cmd ).strip()
        print( "job id: " + str(jiddle_id))
        status = subprocess.check_output( ["tsp", "-s ", str(jiddle_id)] ).strip()
        print ("status " + status )
        date = time.strftime( "%Y/%m/%d %H:%M:%S",time.gmtime())
        print(date)

        cursor.execute("INSERT INTO jobs (user,tag,id,date,status) VALUES (?,?,?,?,?)" , (email,tag,jiddle_id,date,status) )
        connector.commit()
                
  
        while status != "finished":
            status = subprocess.check_output( ["ts", "-s", jiddle_id] ).strip()
            print ("status: " + status)
            cursor.execute( "UPDATE jobs SET status = '" + status + "' WHERE user = '" + email + " AND tag = '" + tag + "'" )
            connector.commit()
            # better: != running and != pending..

            self.update_state(state='PROGRESS',
                              meta={ 'status': status})

            time.sleep(5)
        os.chdir( pwd)
        print( os.getcwd())
        connector.close()
        
    return {'status':'completed'}



def page_url( filename):
    return ( request.base_url + "/" + filename)






@app.route( '/' , methods=['GET', 'POST'])
def index():
    print( sf.func_name() + " go")

    form = RequestForm()
#    form = RequestForm(db='1')

    if request.method=='GET':

        form.email.data = session.get('email','')
        form.sequence.data = session.get('sequence','')
        form.tag.data = session.get('tag','')
        form.db.data = session.get('db','1')
        
        print( sf.func_name() + " get")
        print( sf.func_name() + " " + form.email.data)
        print( sf.func_name() + " " + form.tag.data)
        print( sf.func_name() + " " + form.sequence.data)
        print( sf.func_name() + " " + form.db.data)
        
        return render_template( 'form.html', form=form)
    

    print( sf.func_name() + " post ")
    if form.validate() == False:
        print( sf.func_name() + " errors " )
        flash( 'errors in input (see detailed information above)')
        return render_template( 'form.html', form=form)
    

    #    email = request.form['email']
    session['email'] = form.email.data
    session['tag'] = form.tag.data
    session['sequence'] = form.sequence.data
    session['db'] = form.db.data
    
    print( sf.func_name() + " redirect")
    print( sf.func_name() + " " + session.get('email'))
    print( sf.func_name() + " " + session.get('tag'))
    print( sf.func_name() + " " + session.get('sequence'))
    print( sf.func_name() + " " + session.get('db'))
#    return render_template( 'wait.html', form = form, serialize=Serialize)

    task = submit_and_check_status.apply_async( args=( form.email.data , form.tag.data , form.sequence.data , form.db.data ))
    print( sf.func_name() + " submit send to background, id: " + str( task.id))
    print( sf.func_name() + " forward status location: " +  url_for('taskstatus', task_id=task.id))
    joburl =  url_for('taskstatus', task_id=task.id)
    
    return render_template( 'wait.html', form=form, joburl=joburl)



@app.route('/queue', methods=['GET'])
def queue():

    con = sql.connect("jobs.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from jobs")
    
    rows = cur.fetchall();
    return render_template( "queue.html", rows = rows)
 

#@app.route('/submit', methods=['POST'])
#def submittask():
#    print( sf.func_name() )
#    #email = request.form['email']
#    email = session['email']
#    tag = session['tag']
#    sequence = session['sequence'] 
#    db = session['db']
#    print( sf.func_name() + " " + email )
#    print( sf.func_name() + " " + tag )
#    print( sf.func_name() + " " + sequence )
#    print( sf.func_name() + " " + db )
#    
#    task = submit_and_check_status.apply_async( args=(email,tag,sequence,db))
##    task = submit_and_check_status.apply_async( kwargs={'email':email , 'tag':tag, 'sequence':sequence, 'db':db})
##    task = submit_and_check_status.apply_async()
#    print( sf.func_name() + " submit send to background, id: " + str( task.id))
#    print( sf.func_name() + " forward status location: " +  url_for('taskstatus', task_id=task.id))
#    return jsonify({}), 202, {'Location': url_for('taskstatus', task_id=task.id)}



@app.route('/status/<task_id>')
def taskstatus(task_id):
    print( sf.func_name() + " id: " + task_id)
    task = submit_and_check_status.AsyncResult(task_id)
    print( sf.func_name() + " async result: " + task.state + " " + task.status )
    if task.state == 'PENDING':
        print( sf.func_name() + " pending")
        response = {
            'state': task.state,
            'status': 'not queued'
        }
    elif task.state != 'FAILURE':
        print( sf.func_name() + " running")        
        response = {
            'state': task.state,
            'status': task.info.get('status', '')
        }
    else:
        print( sf.func_name() + " trouble")
        # something went wrong in the background job
        response = {
            'state': task.state,
            'status': str(task.info)  # this is the exception raised
        }
    print( sf.func_name() + " jsonify response")
    return jsonify(response)



@app.route( '/results/<job_id>')
@app.route( '/results/<user>/<job_id>')
def results( job_id, user="unknown"):
    user = sf.QuickFix( user )
    feil = "data/" + user + "/" + job_id + "/protein_prompt.txt"
    all_lines = sf.WriteLines( feil)
    return render_template( 'results.html', lines=all_lines)


@app.route( '/list_results')
def list_results():
    path = "data/"
    mstr = ""
    for root, dirs, files in os.walk( path ):
        if path == root: continue
        root = root[ len(path):]
        root = root.replace('_','@',1) # overliquid
        root = root.replace('_','.')   # overliquid
        
        for name in dirs:
            mstr += "<tr><td>" + root + "</td><td><a href=\"/results/" + root + "/" + name + "\">"  + name + "</a></td></tr>\n"      
    return render_template( 'list_results.html', lines=mstr )
    

@app.route( '/methods' )
def methods():
    return render_template( 'methods.html' )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run( debug=True)
