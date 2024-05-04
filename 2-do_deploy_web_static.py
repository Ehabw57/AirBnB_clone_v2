#!/usr/bin/python3
""" a moudle for do_deploy funciton"""
from fabric.api import local, run, env, put
from os import path

env.hosts = ['54.237.6.218', '52.91.182.139']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy a new static version to my web{01,02} servers"""
    if not path.isfile(archive_path):
        return False

    try:
        archive_name = archive_path[9:-4]
        put(local_path=archive_path, remote_path='/tmp/{}.tgz'.format(
            archive_name))
        run('mkdir -p  /data/web_static/releases/{}'.format(archive_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'.format(
            archive_name, archive_name))
        run('mv /data/web_static/releases/{}/web_static/* \
             /data/web_static/releases/{}/'.format(archive_name, archive_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            archive_name))
        run('rm -rf /tmp/{}.tgz'.format(archive_name))
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/{} \
            /data/web_static/current'.format(archive_name))
    except Exception as e:
        print("Deployment failed!!\n{}".format(e))
        return False

    print('New version deployed!')
    return True
