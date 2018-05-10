#!/usr/bin/python2.7

import os
import re
import collections
import sqlite3
import json
import datetime
import csv
import codecs
import random
from cStringIO import StringIO
from flask import send_file, url_for


def page_url( page ):
    return url_for( 'pages', page=page )

def static_url( filename ):
    return  url_for( 'basic_staticx', filename=filename )

def img_url( filename ):
    return static_url( "img/" + filename )

def js_url( filename ):
    return static_url( "js/" + filename )

def allowed_file(filename, app):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config["ALLOWED_EXTENSIONS"]
        
def generate_filename(length=16):
    'Generates a unique file name containing a-z A-Z 0-9'
    pool = range(48, 57) + range(65, 90) + range(97, 122)
    return ''.join(chr(random.choice(pool)) for _ in range(length))

############################
# helper
############################

class UnicodeCsvWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)





