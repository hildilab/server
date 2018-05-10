
from datetime import datetime,timedelta
import os
import sys

# Multiplied with 1024 two times, so it is mega bytes
max_bytes=100
#max_bytes=max_bytes*1024*1024

# Returns the modification date of a file
def modification_date(fname):
    t = os.path.getmtime(fname)
    return datetime.fromtimestamp(t)

# Deletes Files and Subdirectories older than two weeks
def delete(fname):
	for root, subFolders, files in os.walk(fname,topdown=False):
		for f in files:
			s_dir=os.path.join(root,f)
			then = datetime.now() - modification_date(s_dir)
			now = datetime.now()
			if ((now-then) < now-timedelta(weeks = 1)):
				os.remove(s_dir)
		if (not os.listdir(root)) &(root!=fname):
			os.rmdir(root)


def main(fname):
    delete(fname)

if __name__ == "__main__":
    main('/mnt/bigdisk/development/repos/job/static/tmp/r')
