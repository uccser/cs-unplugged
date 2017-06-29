#!/bin/bash
function cpu_count(){
/docker_venv/bin/python << END
import sys
from render.daemon.utils import  get_recommended_number_of_daemons
sys.exit(get_recommended_number_of_daemons())
END
render_daemons=$?
}

cpu_count
for i in `seq 1 ${render_daemons}`;
do
  /docker_venv/bin/python -m render.daemon --daemon ${i} start &
done

/docker_venv/bin/gunicorn -c render/webserver/gunicorn.conf.py -b :${PORT} render.webserver.wsgi
