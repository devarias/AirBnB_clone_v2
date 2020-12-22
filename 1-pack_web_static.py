#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime


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
