from fabric import task, Connection
import time

@task
def do_pack(c):
    """Creates an archive file for web_static directory"""

    try:
        c.run("mkdir -p versions")
        archiveTime = time.strftime("%Y%m%d%H%M%S")
        c.run(f"tar -czvf versions/web_static_{archiveTime}.tgz web_static/")
        return archiveTime
    except Exception:
        return None

@task
def do_deploy(c, archive_path):
    """Distributes an archive file into a server"""

    fileName = (archive_path.split('.')[0]).split('/')[1]
    archiveFile = f"/tmp/{archive_path.split('/')[1]}"
    dataPath = f"/data/web_static/releases/{fileName}/"
    linkPath = '/data/web_static/current'

    try:
        c.put(archive_path, '/tmp/')
        print("put")
        c.run(f"mkdir -p {dataPath}")
        c.run(f"tar -xzvf {archiveFile} -C {dataPath} --strip-components=1")
        c.run(f"rm {archiveFile}")
        c.run(f"rm {linkPath}")
        c.run(f"ln -s {dataPath} {linkPath} ")

    except Exception as e:
        print(e)
        return False
    return True
