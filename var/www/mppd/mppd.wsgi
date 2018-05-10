APP_PATH = '/home/webit/app/mppd/'
APP_ENV = '' # '/home/arose/dev/envs/bin/activate_this.py'




"""
http://flask.pocoo.org/docs/deploying/mod_wsgi/

Problem: application gives permission errors
Probably caused by your application running as the wrong user. Make sure the folders the application needs access to have the proper privileges set and the application $
"""




if APP_ENV:
    activate_this = APP_ENV
    execfile(activate_this, dict(__file__=activate_this))

import os
os.chdir(APP_PATH)

import sys
if APP_PATH not in sys.path:
    sys.path.insert(0, APP_PATH)
sys.stdout = sys.stderr

from MPPD_local import app as application


