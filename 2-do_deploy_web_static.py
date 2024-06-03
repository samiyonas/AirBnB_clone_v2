#!/usr/bin/python3
""" serving a website using Fabric """
from datetime import datetime
from fabric.api import local, env, run, put, sudo
import os


env.hosts = ["100.25.130.63", "100.25.200.147"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/web01"


def do_pack():
    """ pack the web static """
    local("mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    arcf = "versions/web_static_{}.tgz".format(time)
    local("tar -cvzf {} web_static".format(arcf))

    return arcf

def do_deploy(archive_path):
    """ deploy the web static succesfully """
    if os.path.exists(archive_path) is False:
        return False
    try:
        run("mkdir -p /tmp/")
        put(archive_path, "/tmp/")
        arch_dir = archive_path.split("/")[1].split(".")[0]
        hp = "/data/web_static/releases/{}/web_static/*".format(arch_dir)
        ft = archive_path.split("/")[1]
        full_path = "/data/web_static/releases/{}".format(arch_dir)
        run("mkdir -p {}".format(full_path))
        run("tar -xzvf /tmp/{} -C {}".format(ft, full_path))
        run("rm -rf /tmp/{}".format(ft))
        run("mv {} /data/web_static/releases/{}/".format(hp, arch_dir))
        run("rm -rf /data/web_static/current/")
        run("ln -s {}/ /data/web_static/current".format(full_path))
        return True
    except Exception:
        return False
