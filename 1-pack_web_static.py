#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static directory."""
from fabric.api import local
import time


def do_pack():
    """Generate an tgz archive from web_static directory"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception as e:
        return None
