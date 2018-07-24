import sqlite3

conn = sqlite3.connect('jobs.db')
print "Opened database successfully";
c = conn.cursor()
cmd = "SELECT * FROM jobs WHERE strftime('%s',date) <= strftime( '%s', datetime('now','-2 minutes'))"
cmd = "SELECT *, time( strftime( '%s', datetime('now')) - strftime('%s','2018-07-24 13:00:00') , 'unixepoch') FROM jobs"
cmd = "SELECT replace(date,'/','-'), datetime('now'), strftime('%s', datetime('now') ) - strftime('%s', replace(date,'/','-'))  FROM jobs"
cmd = "SELECT replace(date,'/','-'), datetime('now'), time( strftime('%s', datetime('now') ) - strftime('%s', replace(date,'/','-')) , 'unixepoch')  FROM jobs"

# select entries older than X seconds:
cmd = "SELECT * FROM jobs WHERE strftime('%s', datetime('now') ) - strftime('%s', replace(date,'/','-')) > 6000"

# delete entries older than X seconds:
#cmd = "DELETE FROM jobs WHERE strftime('%s', datetime('now') ) - strftime('%s', replace(date,'/','-')) > 6000"

cmd = "SELECT * FROM jobs"

#cmd = "UPDATE jobs SET status = 'finished' WHERE status = 'queued'"

print cmd

c.execute( cmd )
conn.commit()

for l in c.fetchall():
    print l

conn.close()
