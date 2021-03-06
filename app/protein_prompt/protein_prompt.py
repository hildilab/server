import time, os, subprocess
import sqlite3 as sql

from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify, current_app, send_file
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from threading import Thread

import sequence_functions as sf
from request_form import RequestForm

app = Flask( __name__ )

app.config['SECRET_KEY'] = 'topf-sekret'
app.config['MAIL_SERVER'] = 'smtp.1und1.de'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] =  os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] =  os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[ProteinPrompt]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['USER_DATA_DIR'] = basedir + "/data/" 
app.config['APP_PATH'] = basedir


bootstrap = Bootstrap(app)
mail = Mail( app )




def send_email(email, tag, mess, url):
    with app.app_context():

        print( sf.func_name())
        subject =  tag + " " + mess
        template = 'mail/link'
        msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                      sender=app.config['FLASKY_MAIL_SENDER'], recipients=[email])
        msg.body = render_template(template + '.txt', email=email, tag=tag, mess=mess, url=url )
        msg.html = render_template(template + '.html', email=email, tag=tag, mess=mess, url=url )
        mail.send(msg)


    
def wait_and_notify( app, email, tag, sid, url):
    with app.app_context():
        print( sf.func_name())
        status = {'status':'xxx'}
        while status['status'] != "finished":
            time.sleep(30)
            print( sf.func_name() + " update")
            status = update_status( sid )
        if status['error'] == '0':
            mess = "completed successfully"
        else:
            mess = "failed"
        send_email( email, tag, mess, url)


        
def send_email_upon_termination( email, tag, sid ):
    print( sf.func_name())
    # create new thread to send to background
    url = url_for('results',user=email,job_id=tag, _external=True)
    thr = Thread( target=wait_and_notify, args=[app, email, tag, sid, url] )
    thr.start()
    return thr



def submit( email, tag, sequence, db):
    print ( "now entered submit:" + current_app.name )
#    os.chdir( app.config['APP_PATH'] )
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

#    os.chdir( user_dir )
    job_dir = user_dir + "/" + email + "/" + tag

    print( job_dir )
    if os.path.isdir( job_dir):
        print ( "dir exists")
        return {'status':'exists' , 'id':'-99999', 'error':'-99999'}
    else:
        os.makedirs( job_dir )
        print( job_dir + " created")
#    os.chdir( job_dir )
    with open( job_dir + '/protein_prompt.txt','w') as f:
        f.write( "fake.fa 15 AABCDEABCDEBCDE 0.4 \n")
        f.write( "cake.fa 105 ABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDEABCDE 0.5 \n")
        f.write( "bake.fa 5 ABCDE 1.5 \n")

    print( sf.func_name() + " send to queue" )
    #cmd = "tsp rf -seq " + sequence + " -db " + db + " -out " + job_dir + "/protein_prompt.txt"
    cmd = ["tsp", "sleep", "10"]
    jiddle = subprocess.check_output( cmd ).strip()
    print( "job id: " + jiddle)
    status = subprocess.check_output( ["tsp", "-s" , str(jiddle)] ).strip()
    print ("status " + status )
    date = time.strftime( "%Y-%m-%d %H:%M:%S",time.gmtime())
    print(date)

    print ( "INSERT INTO jobs (user,tag,id,date,status) VALUES (?,?,?,?,?)" , (email,tag,jiddle,date,status) )
    cursor.execute("INSERT INTO jobs (user,tag,id,date,status) VALUES (?,?,?,?,?)" , (email,tag,jiddle,date,status) )
    connector.commit()

#    os.chdir( pwd)
    print( "now: " + os.getcwd() + " should have retured to base dir")
    connector.close()
        
    return { 'status':status , 'id':jiddle }


def update_status( jiddle ):
    print( sf.func_name())
    connector = sql.connect("jobs.db")
    cursor = connector.cursor()
    status = subprocess.check_output( ["tsp", "-s" , str(jiddle)] ).strip()
    error = ""
    if status == "finished":
        error = subprocess.check_output( ["tsp", "-i" , str(jiddle)] )
        print(sf.func_name() + " " + error)
        id1 = error.find( "exit code") + 10
        id2 = error.find( '\n' )
        error = error[id1:id2].strip()
        print(sf.func_name() + " error-code: <" + error + ">")
        
    cmd = "UPDATE jobs SET status = '" + status + "' WHERE id = '" + str(jiddle) + "'"
    print( cmd )
    cursor.execute( cmd )
    connector.commit()
    connector.close()
    return { 'status':status , 'error':error}
            

def update_all():
    print( sf.func_name())
    connector = sql.connect("jobs.db")
    cursor = connector.cursor()
    status = {}
    lines = subprocess.check_output( ["tsp"] ).split('\n')
    print( str(len(lines)) + " entries" )
    for l in lines:
        print(l)
        l = l.strip()
        if len(l) < 5 or "ID" in l: continue
        c = l.split()
        status[ c[0] ] = c[1]
        
    for k,v in status.iteritems():
        cmd = "UPDATE jobs SET status = '" + v + "' WHERE id = '" + k + "'"
        print( cmd )
        cursor.execute( cmd )
    connector.commit()
        
    connector.close()
    return status
   



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

    status = submit( form.email.data , form.tag.data , form.sequence.data , form.db.data )
    print( sf.func_name() + " submit send to background, id: " + str( status['id'] ))
    print( sf.func_name() + " forward status location: " +  url_for('taskstatus', task_id=status['id']))
    joburl =  url_for('taskstatus', task_id = status['id'] )
    if int( status['id'] ) < 0 :
        flash( "submission failed" )
        return render_template( 'form.html', form=form)

    # start background process waiting for termination of calculation to send email
    if form.email.data != "anonymous":
        send_email_upon_termination( form.email.data, form.tag.data, status['id'] )
    
    return render_template( 'wait.html', form=form, joburl=joburl)



@app.route('/queue', methods=['GET'])
def queue():

    update_all()
    
    con = sql.connect("jobs.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from jobs")
    con.commit()
    rows = cur.fetchall();
    con.close()
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
    status = update_status(task_id)
    return jsonify( status )



@app.route( '/results/<job_id>')
@app.route( '/results/<user>/<job_id>')
def results( job_id, user="anonymous"):
    user = sf.QuickFix( user )
    data = app.config['USER_DATA_DIR']
    print( sf.func_name() + " datadir: " + str(data))
    feil = data + "/" + user + "/" + job_id + "/protein_prompt.txt"
    all_lines = sf.WriteLines( feil)
    feil = "../../downloads/" + user + "/" + job_id + "/result.txt"
    return render_template( 'results.html', lines=all_lines, user=user, job_id=job_id,result=feil)


@app.route( '/downloads/<user>/<job_id>/<file_name>')
def download( job_id, user, file_name):

    data = app.config['USER_DATA_DIR']
    feil = data + "/" + user + "/" + job_id + "/protein_prompt.txt"
    print( sf.func_name() + " " + feil)
    try:
        return send_file( feil, attachment_filename='results.txt')
    except Exception as e:
        return str(e)



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
            mstr += "<tr><td>" + root + "</td><td><a href=\"" + url_for( 'results' , user=root, job_id=name ) + "\">"  + name + "</a></td></tr>\n"      
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
    app.run()
#    app.run( debug=True)
