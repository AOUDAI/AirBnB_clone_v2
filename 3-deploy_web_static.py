#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static directory."""
from fabric.api import local, run, put, env
import time

env.hosts = ['100.35.193.96', '100.26.169.112']


def do_pack():
    """Generate an tgz archive from web_static directory"""

    archiveTime = time.strftime("%Y%m%d%H%M%S")
    archivePath = f"versions/web_static_{archiveTime}.tgz"

    try:
        local("mkdir -p versions")
        local(f"tar -czvf {archivePath} web_static/")
        return archivePath
    except Exception:
        return None


def do_deploy(archive_path):
    """
    copies archive file from local to my webservers
    """

    fileName = (archive_path.split('.')[0]).split('/')[1]
    archiveFile = f"/tmp/{archive_path.split('/')[1]}"
    dataPath = f"/data/web_static/releases/{fileName}/"
    linkPath = '/data/web_static/current'

    try:
        put(archive_path, '/tmp/')
        run(f"mkdir -p {dataPath}")
        run(f"tar -xzvf {archiveFile} -C {dataPath} --strip-components=1")
        run(f"rm {archiveFile}")
        run(f"rm {linkPath}")
        run(f"ln -s {dataPath} {linkPath} ")
    except Exception:
        return False


def deploy(c):
    """ create and distributes an archive to a web server"""

    archivePath = do_pack()

    if archivePath:
        return do_deploy(archivePath)
    else:
        return False
