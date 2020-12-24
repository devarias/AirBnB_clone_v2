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
    with lcd("versions"):
        number = int(number)
        if number == 0 or number == 1:
            number = 1
        n = str(number + 2)
        local("mkdir test")
        local("ls -1t | grep -v 'test' | tail -n +{} > files.tmp".format(n))
        local("rm -rf `cat files.tmp`")
        local("rm -r test")
        local("rm files.tmp")
    with cd("/data/web_static/releases/"):
        run("ls -1t | grep -v 'test' | tail -n +{} > files.tmp".format(n))
        run("rm -rf `cat files.tmp`")
        run("rm files.tmp")
