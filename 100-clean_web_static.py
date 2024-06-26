#!/usr/bin/python3
""" serving a website using Fabric """
from datetime import datetime
from fabric.api import local, env, run, put, sudo
from fabric.context_managers import cd
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
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """ all in one """
    arcf = do_pack()
    if arcf is None:
        return False
    return do_deploy(arcf)


def do_clean(number):
    """ clean up shit """
    out = local("ls versions/ | sort", capture=True)
    dellist = out.split("\n")
    num = int(number)
    if num == 0:
        num = 1
    for i in range(len(dellist) - num):
        local("rm versions/{}".format(dellist[i]))
    with cd("/data/web_static/releases"):
        remoteout = run("ls | sort").split()
        remoteout = [a for a in remoteout if "web_static_" in a]
        for i in range(len(remoteout) - num):
            run("rm -r /data/web_static/releases/{}".format(remoteout[i]))
