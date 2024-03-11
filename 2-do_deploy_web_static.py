#!/usr/bin/python3
""" Defines do_deploy function"""

from fabri.api import put, env, run


def do_deploy(archive_path):
    """ Distributes an archive to a web server.
    
    Args:
        archive_path (str): the path to archive file
    Return:
        True in success, otherwise False.
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
    return True
