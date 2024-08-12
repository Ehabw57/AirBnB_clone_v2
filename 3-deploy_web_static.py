#!/usr/bin/python3
"""I dont know what to say just copying this fuction becuse
i dont care about fabric"""

from fabric.api import env, local, run, put, runs_once
from datetime import datetime
import os
env.hosts = ['18.234.145.174', '34.202.158.120']


@runs_once
def do_pack():
    """ blah balh blah
    balhs
    """
    date_now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = 'versions/web_static_{}.tgz'.format(date_now)
    local('mkdir -p versions')

    status = local(
        'tar -cvzf {} web_static'.format(archive_path))

    if status.failed:
        return None
    else:
        return archive_path


def do_deploy(archive_path):
    """ balh again and again """

    if os.path.isfile(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")[-1]
        path = "/data/web_static/releases"
        put("{}".format(archive_path), "/tmp/{}".format(archive))
        folder = archive.split(".")
        run("mkdir -p {}/{}/".format(path, folder[0]))
        new_archive = '.'.join(folder)
        run("tar -xzf /tmp/{} -C {}/{}/"
            .format(new_archive, path, folder[0]))
        run("rm /tmp/{}".format(archive))
        run("mv {}/{}/web_static/* {}/{}/"
            .format(path, folder[0], path, folder[0]))
        run("rm -rf {}/{}/web_static".format(path, folder[0]))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/{} /data/web_static/current"
            .format(path, folder[0]))
        return True
    except Exception as e:
        return False


def deploy():
    """deployt he website aleady"""

    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
