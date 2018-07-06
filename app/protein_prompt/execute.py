import subprocess, os

exec = "path/rf.sh"

def Execute( cmd):
    #cmd = "tsp sleep 45"
    p = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = []
    while True:
        line = p.stdout.readline()
        out.append(line)
        #print line,
        if line == '' and p.poll() != None:
            break
    out = ''.join(out).strip()
    return out


def Submit( cmd):
    cmd = "tsp " + cmd
    return int(Execute(cmd))


def IsRunning( pid):
    cmd = "tsp -i " + str(pid)
    out = Execute( cmd)
    if out[:4] == "Exit":
        return False
    return True
    

def RunJob( seq, user, tag):
    jdir = DATA_DIR + "results/" + user + "/" + tag
    if not os.path.exists(jdir):
        os.makedirs( jdir)

    os.chdir( jdir)

    existing = os.listdir( "." )
    if len(existing) > 0:
        #print "already existing, exit"
        exit(1)

    cmd = executable + seq
    pid = Submit( cmd)
    
    os.chdir( "../../..")
    return pid



#    with open( "testx.tmp", 'w') as f:
#        f.write( "hallo welt...\n")
#    pid = -1
    #read output of ts:
    # mkdir results/user/tag
    # cd ..
    # execute: ts rf.sh sequence
    # send second ts for message?? env var: export FL_JOB=1, andere liesst?
    # check for status
    # return upon completion
#    time.sleep(30)
#    return pid

