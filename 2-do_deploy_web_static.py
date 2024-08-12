#!/usr/bin/python3
""" a moudle for do_deploy funciton"""
from fabric.api import run, env, put
from os import path

env.hosts = ['54.237.6.218', '52.91.182.139']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy a new static version to my web{01,02} servers"""
    if not path.isfile(archive_path):
        return False

    archive_name = archive_path.split('/')[1].split('.')[0]
    result = put(archive_path, '/tmp/')
    if result.failed:
        return False

    result = run('mkdir -p  /data/web_static/releases/{}'.format(archive_name))
    if result.failed:
        return False

    result = run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
        archive_name, archive_name))
    if result.failed:
        return False

    result = run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(archive_name, archive_name))
    if result.failed:
        return False

    status = run(
        'rm -rf /data/web_static/releases/{}/web_static'.format(archive_name))
    if status.failed:
        return False

    status = run('rm -rf /data/web_static/current')
    if status.failed:
        return False

    result = run('ln -s /data/web_static/releases/{} \
        /data/web_static/current'.format(archive_name))
    if result.failed:
        return False

    print('New version deployed!')
    return True
