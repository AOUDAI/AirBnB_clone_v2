#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
fab -f 2-do_deploy_web_statipy do_deploy:archive_path=filepath
    -i private-key -u user
"""

from os.path import exists
from fabriapi import put, run, env

env.hosts = ['100.35.193.96', '100.26.169.112']


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
