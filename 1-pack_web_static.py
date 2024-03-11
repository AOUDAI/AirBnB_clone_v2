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
