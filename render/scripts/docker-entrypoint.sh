#!/bin/bash
export RENDER_DAEMONS=$( nproc --all )
for i in `seq 1 ${RENDER_DAEMONS}`;
do
  /docker_venv/bin/python ./render.py --daemon ${i} start &
done

/docker_venv/bin/gunicorn -c ./gunicorn.conf.py -b :${PORT} wsgi
