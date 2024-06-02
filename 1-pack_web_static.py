#!/usr/bin/python3
""" compress before sending it to the server """
from datetime import datetime
from fabric.api import local


@task
def do_pack():
    """ pack the web static """
    local("mkdir -p /versions")
    time = datetime.now().strftime("%Y%m%d%H%M")
    arcf = "/versions/web_static_{}.tgz".format(time)
    result = local(f"tar -czvf {arcf} /web_static/", capture=True)

    if result.failed:
        return None
    else:
        return arcf
