#!/bin/bash
export RENDER_DAEMONS=$( nproc --all )
echo "export RENDER_DAEMONS=${RENDER_DAEMONS}" >> ~/.bashrc
for i in `seq 1 ${RENDER_DAEMONS}`;
do
  /docker_venv/bin/python -m render.daemon --daemon ${i} start &
done

/docker_venv/bin/gunicorn -c render/webserver/gunicorn.conf.py -b :${PORT} render.webserver.wsgi
