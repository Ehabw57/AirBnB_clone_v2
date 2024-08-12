#!/usr/bin/python3
""" fabic script to clean up old archives"""

from fabric.api import local, env, run

env.hosts = ['54.237.6.218', '52.91.182.139']


def do_clean(number=0):
    """deletes out-of-date archives yes """
    number = int(number)
    if number < 2:
        number = 2
    else:
        number += 1
    local('ls -dt versions/* | tail -n +{} | xargs rm -rf'.format(number))
    run('ls -dt /data/web_static/releases/* |\
         tail -n +{} | xargs rm -rf'.format(number))
