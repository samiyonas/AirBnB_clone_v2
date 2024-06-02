#!/usr/bin/python3
""" compress before sending it to the server """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ pack the web static """
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    arcf = "versions/web_static_{}.tgz".format(time)
    local("tar -cvzf {} web_static".format(arcf))

    return arcf
