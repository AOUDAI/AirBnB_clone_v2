#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """

    env.hosts = ["100.25.193.96", "100.26.169.112"]

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)

# #!/usr/bin/python3
# """Generates a .tgz archive from the contents of the web_static directory."""
# from fabric.api import local, run, put, env
# import time

# env.hosts = ['100.35.193.96', '100.26.169.112']


# def do_pack():
#     """Generate an tgz archive from web_static directory"""

#     archiveTime = time.strftime("%Y%m%d%H%M%S")
#     archivePath = f"versions/web_static_{archiveTime}.tgz"

#     try:
#         local("mkdir -p versions")
#         local(f"tar -czvf {archivePath} web_static/")
#         return archivePath
#     except Exception:
#         return None


# def do_deploy(archive_path):
#     """
#     copies archive file from local to my webservers
#     """

#     fileName = (archive_path.split('.')[0]).split('/')[1]
#     archiveFile = f"/tmp/{archive_path.split('/')[1]}"
#     dataPath = f"/data/web_static/releases/{fileName}/"
#     linkPath = '/data/web_static/current'

#     try:
#         put(archive_path, '/tmp/')
#         run(f"mkdir -p {dataPath}")
#         run(f"tar -xzvf {archiveFile} -C {dataPath} --strip-components=1")
#         run(f"rm {archiveFile}")
#         run(f"rm {linkPath}")
#         run(f"ln -s {dataPath} {linkPath} ")
#     except Exception:
#         return False


def deploy(c):
    """ create and distributes an archive to a web server"""

    archivePath = do_pack()

    if archivePath:
        return do_deploy(archivePath)
    else:
        return False
