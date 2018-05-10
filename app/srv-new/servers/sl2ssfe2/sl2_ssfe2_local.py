#!/usr/bin/env python

import os
import tempfile
import zipfile
import collections
import json
import sys
import re
from cStringIO import StringIO
import csv

import datetime
import sqlite3
from flask import (
    Flask, request, render_template,
    send_from_directory, send_file, url_for
)
sys.path.append(
    os.path.split( os.path.split( os.path.abspath( __file__ ) )[0])[0]
)

from static.local import (
    page_url, static_url, img_url, js_url, UnicodeCsvWriter
)


cfg_file = 'app.cfg'

app = Flask( __name__ )
app.config.from_pyfile( cfg_file )

APP_PATH = app.config.get("APP_PATH", "")
BASIC_PATH = app.config.get("BASIC_PATH", "")
JOB_URL = app.config.get("JOB_URL", "")
DATABASE_PATH = app.config.get("DATA_FOLDER", "")
PROVI_URL = app.config["PROVI_URL"]
PIWIK_TRACKER_ID = app.config["PIWIK_TRACKER_ID"]
VERSION = "1.1"

def get_nop( app ):
    with sqlite3.connect( app.config['DATABASE'] ) as conn:
        c = conn.cursor()
        c.execute('SELECT COUNT(*) FROM InfoRecord')
        nop = c.fetchone()[0]         
    return nop

def get_names( app ):
    with sqlite3.connect( app.config['DATABASE'] ) as conn:
        c = conn.cursor()
        c.execute('PRAGMA table_info(InfoRecord)')
        names = c.fetchall()
    return [ row[1] for row in names ]

def read_entries( app, keywds=None, sortby='pdb_id', 
                    direction='ASC', start=0, limit=0, database='DATABASE'):
    where = []
    pdbids = ""
    if database==1 or database==None or database=="DATABASE" or database=="undefined":
        database = app.config['DATABASE']
    else:
        database = os.path.join(app.config['JOB_FOLDER'], database, 'voronoia.sqlite')
    def phrase( q ):
        return ("( "
            "pdb_id = \'%(q)s\' COLLATE NOCASE OR "
            "pdb_zscorerms like \'%%%(q)s%%\' COLLATE NOCASE OR "
            "pdb_resolution like \'%%%(q)s%%\' COLLATE NOCASE OR "
            "pdb_title like \'%%%(q)s%%\' COLLATE NOCASE OR "
            "pdb_experiment like \'%%%(q)s%%\' COLLATE NOCASE"
        " )") % { "q": q }

    if keywds:
        # # split by whitespace or comma unless enclosed by 
        # # double or single quotes
        # keywds = re.findall( 
        #     r"[^\s,\"']+|\"[^\"]*\"|'[^']*'", keywds.upper()
        # )
        # keywds = [ k.strip("'\"") for k in keywds ]
        # print keywds
        # pdbids = [ x for x in keywds if len(x)==4 ]
        s = re.sub( "(\s+OR\s+)", " ", keywds )
        s = re.sub( "(\s+AND\s+|\s?\+\s?)", "+", s )
        print s

        x = re.findall( 
            r"[^\s,\"']+|\"[^\"]*\"|'[^']*'", s
        )
        print x

        x2 = []
        ix = iter(x)
        for xx in ix:
            if xx=="+":
                x2[-1] += xx + next( ix )
            elif xx[-1]=="+":
                x2.append( xx + next( ix ) )
            elif xx[0]=="+":
                x2[-1] += xx
            else:
                x2.append( xx )
        print x2

        q_or = []
        for _or in x2:
            q_and = []
            for _and in _or.split("+"):
                q_and.append( phrase( _and.strip("'\"") ) )
            q_or.append( "( " + " AND ".join( q_and ) + " )" )
        q_or = "( " + " OR ".join( q_or ) + " )"
        where.append( q_or )


    pdbids = ""
    if pdbids:
        where.append( 
            " OR ".join([ 
                "pdb_id = \'%s\' COLLATE NOCASE" % p for p in pdbids 
            ])
        )
   
    # if keywds:
    #     where.append( 
    #         " OR ".join([ 
    #             (   
    #                 "pdb_keywords like \'%%%s%%\' COLLATE NOCASE OR "
    #                 "pdb_title like \'%%%s%%\' COLLATE NOCASE OR "
    #                 "mpstruc_subgroup like \'%%%s%%\' COLLATE NOCASE OR "
    #                 "mpstruc_name like \'%%%s%%\' COLLATE NOCASE OR "
    #                 "opm_family like \'%%%s%%\' COLLATE NOCASE"
    #             ) % ( k, k, k, k, k ) 
    #             for k in keywds 
    #         ])
    #     )
    
    if where:
        where = "WHERE (" + ( ") OR (".join( where ) ) + ")"
    else:
        where = ""

    
    order_clause = "ORDER BY %s %s" % ( sortby, direction )
    limit_clause = "LIMIT %i, %i" % ( start, limit) if limit else ""

    query = (
        "SELECT * "
        "FROM VoronoiaDbRecord "
        "" + where + ""
        " " + order_clause + ""
        " " + limit_clause + ""
    )
    query_count = (
        "SELECT COUNT(*) "
        "FROM VoronoiaDbRecord "
        "" + where + ""
    )

    print query
    
    pdb_table = []
    with sqlite3.connect( database ) as conn:
        c = conn.cursor()
        for row in c.execute( query ):
            pdb_table.append( row )
   
        c.execute( query_count )
        count = c.fetchone()[0]

    return count, pdb_table


def query_static(app, request, NAMES):
    count, pdb_table = read_entries(
        app,
        keywds=request.args.get('keywds'),
        sortby=request.args.get('sortby', 'pdb_id'),
        direction=request.args.get('dir', 'ASC'),
        start=int( request.args.get('start', 0) ),
        limit=int( request.args.get('limit', 0) ),
        database = request.args.get('database'),
    )
    today = datetime.date.today().isoformat()
    sele = request.args.get('sele')
    if sele:
        sele = map( int, sele.split(",") )
        pdb_table = [ x for i, x in enumerate( pdb_table ) if i in sele ]
    if request.args.get('csv'):
        str_io = StringIO()
        csv_writer = UnicodeCsvWriter(
            str_io, delimiter=',', 
            quotechar='"', quoting=csv.QUOTE_ALL
        )
        csv_writer.writerow( NAMES )
        csv_writer.writerows( pdb_table )
        str_io.seek(0)
        return send_file(
            str_io,
            attachment_filename="v4rna_query_%s.csv" % today,
            as_attachment=True
        )
    else:
        return json.dumps( collections.OrderedDict({
            "start": int( request.args.get('start', 0) ),
            "hits": count,
            "names": NAMES,
            "results": pdb_table,
            "retrieved": today
        }))

NOP = get_nop( app )
NAMES = get_names( app )


def srv_static_url( filename ):
    return url_for( 'srv_staticx', filename=filename )

def srv_img_url( filename ):
    return srv_static_url( "img/" + filename )

def srv_files_url( filename ):
    return srv_static_url( "files/"  + filename)

@app.route('/basicstatic/<path:filename>')
def basic_staticx( filename ):
    return send_from_directory(
        os.path.join( BASIC_PATH, "static/" ), filename, as_attachment=True
    )
@app.route('/static/<path:filename>')
def srv_staticx(filename):
    return send_from_directory(
        os.path.join( APP_PATH, "static/" ), filename, as_attachment=True
    )

@app.route('/query', methods=['POST','GET'])
def query():
    return query_static(app, request, NAMES)

def provi_url( pdb_id ):
    return "%s?dir=v4rna&file=%s/voronoia_ori/voronoia.provi" % (
        PROVI_URL, pdb_id
    )

### changeable
@app.route('/results/<ids>', methods=['GET', 'POST'])
def results( ids ):
    page = 'results'
    return render_template(
        '%s.html' % page, nop=NOP, version=VERSION,
        page=page_url, v4rna_static=srv_static_url, static=static_url, v4rna_img=srv_img_url,
        img=img_url, js=js_url, database = ids, job_path = JOB_URL,
        provi_url=PROVI_URL, piwik_tracker_id=PIWIK_TRACKER_ID
    )   


@app.route('/', defaults={'page': "SL2-SSFE2.0"}, methods=['GET', 'POST'])
@app.route('/<string:page>/', methods=['GET', 'POST'])
def pages( page ):
    if page not in [
        "welcome", "grid", "calculation", "manual", "method",
        "statistics", "faq", "refs", "links", "wait", "results", "SL2-SSFE2.0"
    ]:
        page = "SL2-SSFE2.0"
 
    return render_template(
        '%s.html' % page, nop=NOP, version=VERSION,
        page=page_url, v4rna_static=srv_static_url, static=static_url, v4rna_img=srv_img_url,
        img=img_url, v4rna_files=srv_files_url, js=js_url, job_path=JOB_URL,
        provi_url=PROVI_URL, 
    )

@app.route('/download/<string:pdb_id>')
def download(pdb_id):
    fp = tempfile.NamedTemporaryFile( "w+b" )
    datapath = os.path.join( DATABASE_PATH, pdb_id )
    with zipfile.ZipFile(fp, 'w', zipfile.ZIP_DEFLATED) as fzip:
        files = os.path.join( datapath, "voronoia_ori", '%s.vol' % pdb_id)
        fzip.write( 
            files, os.path.basename(files)
        )
        fzip.writestr(
            'voronoia_records.json',
            json.dumps( 
                collections.OrderedDict( 
                    zip( NAMES, read_entries( app )[1][0] ) 
                ),
                indent=4
            )
        )
        fzip.writestr(
            "README.txt",
            (
                '%(pdb_id)s.vol: '
                    'PDB file including the structure,'
                    'the Van-der-Waals-volume and '
                    'the solvent-excluded-volume.\n\n'
                'voronoia_records.json: '
                    'JSON file including the V4RNA database entry. '
                '' % { "pdb_id": pdb_id }
            )
        )
    return send_file(
        fp.name,
        attachment_filename="%s_v4rna.zip" % pdb_id,
        as_attachment=True
    )


############################
# main
############################

if __name__ == '__main__':
    app.run( 
        debug=app.config.get('DEBUG', False),
        host=app.config.get('HOST', '127.0.0.1'),
        port=app.config.get('PORT', 4223),
        extra_files=['app.cfg']
    )


