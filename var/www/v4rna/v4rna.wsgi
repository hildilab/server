#####
# configuration for the mppd wsgi app

# path to the directory where MPPD_local.py is located
#APP_PATH = '/home/webit/app/srv-new/servers/v4rna'
APP_PATH = '/home/webit/app/v4rna'

# leave empty if no virtualenv is needed
# APP_ENV = '/home/arose/dev/envs/bin/'
APP_ENV = ''
 



#####
# do not change anything below unless you are sure
# http://flask.pocoo.org/docs/deploying/mod_wsgi/


import os

if APP_ENV:
    activate_this = os.path.join( APP_ENV, 'activate_this.py' )
    execfile( activate_this, dict( __file__=activate_this ) )

os.chdir( APP_PATH )

import sys
if APP_PATH not in sys.path:
    sys.path.insert( 0, APP_PATH )
sys.stdout = sys.stderr

from V4RNA_local import app as application


