#!/usr/bin/python3
"""Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean"""

from fabric.contrib import files
from fabric.api import env, put, run, local, lcd, cd
from os.path import exists, isdir
from datetime import datetime

env.hosts = ['34.74.218.65', '35.190.174.10']


def do_clean(number=0):
    """function to that delete out-of-date archives"""
    if int(number) < 2:
        number = "3"
    else:
        number = "4"
    with lcd("versions"):
        local("ls -1t | tail -n +{} > files.tmp".format(number))
        local("rm -rf `cat files.tmp`")
        local("rm files.tmp")
    with cd("/data/web_static/releases/"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
