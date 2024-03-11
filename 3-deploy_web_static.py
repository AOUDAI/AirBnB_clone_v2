#!/usr/bin/python3
"""
With Facric , creates a tgz archive
from web_static content folder
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.236.171.16', '3.237.45.190']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Creates a tgz archive using fabric"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as ex:
        return None


def do_deploy(archive_path):
    """deploy web static with fabric"""
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_excep = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, no_excep))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_excep))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_excep))
        run('sudo rm -rf {}{}/web_static'.format(path, no_excep))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_excep))
        return True
    except BaseException:
        return False


def deploy():
    """ do path an do deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

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


# def deploy(c):
#     """ create and distributes an archive to a web server"""

#     archivePath = do_pack()

#     if archivePath:
#         return do_deploy(archivePath)
#     else:
#         return False
