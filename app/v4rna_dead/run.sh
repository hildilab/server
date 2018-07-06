#!/bin/sh

cd `dirname $0`

python ./scripts/paster.py serve biobench_wsgi.ini $@
