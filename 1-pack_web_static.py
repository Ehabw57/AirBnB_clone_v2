#!/usr/bin/python3
""" pack all content of the dir web_statics"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """pack all the contents in web_static"""
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path = 'versions/web_static_{}.tgz'.format(date)

    local('mkdir -p versions')
    result = local('tar -cvzf {} web_static'.format(path))

    if result.succeeded:
        return path
    else:
        return None
