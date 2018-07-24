import subprocess, sys

cmd =  [ "tsp", "-s", sys.argv[1] ]
#cmd = [ "tsp","-s " +  sys.argv[1] ]

print cmd

print  subprocess.check_output( cmd )
