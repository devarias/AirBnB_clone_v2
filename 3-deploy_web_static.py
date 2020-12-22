#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy"""

from fabric.contrib import files
from fabric.api import env, put, run, local
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['34.74.218.65', '35.190.174.10']


def do_pack():
    """The function do_pack must return the archive path
    if the archive has been correctly generated.
    Otherwise, it should return None
    """
    file = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    folder = "versions/"
    local("mkdir -p " + folder)
    check = local("tar -cvzf {}{} web_static".format(folder, file))
    if check.succeeded:
        return folder + file
    return None


def do_deploy(archive_path):
    """function, using the new path of the new archive"""
    if not exists(archive_path):
        return False

    dataPath = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dst = dataPath + name
    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dst))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dst))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dst, dst))
        run('rm -rf {}/web_static'.format(dst))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dst))
        return True
    except:
        return False


def deploy():
    """function to call the function do_pack and do_deploy in one call"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
