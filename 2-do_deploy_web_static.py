#!/usr/bin/python3
"""
Fabric script to deploy tgz archive
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=filepath
    -i private-key -u user
"""

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['35.243.128.200', '3.239.120.96']


def do_deploy(archive_path):
    """
    copies archive file from local to my webservers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False


# #!/usr/bin/python3
# """ Defines do_deploy function"""

# from fabri.api import put, env, run


# def do_deploy(archive_path):
#     """Distributes an archive to a web server.

#     Args:
#         archive_path (str): The path of the archive to distribute.
#     Returns:
#         If the file doesn't exist at archive_path or an error occurs - False.
#         Otherwise - True.
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
#     return True
