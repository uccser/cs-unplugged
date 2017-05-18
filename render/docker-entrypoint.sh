#!/bin/bash
for i in `seq 1 $( nproc --all )`;
do
  /docker_venv/bin/python ./render.py --daemon ${i} start &
done

/docker_venv/bin/gunicorn -c ./gunicorn.conf.py -b :${PORT} wsgi
