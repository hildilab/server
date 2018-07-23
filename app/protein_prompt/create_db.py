import sqlite3

conn = sqlite3.connect('jobs.db')
print "Opened database successfully";

conn.execute('CREATE TABLE jobs (user TEXT, tag TEXT, id INTEGER, date TEXT, status TEXT )')
print "Table created successfully";
conn.close()
