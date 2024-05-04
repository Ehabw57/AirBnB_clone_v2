#!/usr/bin/python3
""" pack all content of the dir web_statics"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """pack all the contents in web_static"""
    local('mkdir -p versions')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(date)
    result = local('tar -cvzf {} web_static'.format(path))

    if result.succeeded:
        return path
    else:
        return None
