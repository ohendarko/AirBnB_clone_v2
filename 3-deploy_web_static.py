#!/usr/bin/python3
"""distributes an archive to your web servers,
using the function do_deploy"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.145.240.142", "100.26.238.188"]
env.user = "ubuntu"


def do_pack():
    """
    Function that Generates a .tgz archive
    """
    local("mkdir -p versions")
    src = "web_static/"
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    out = f"versions/web_static_{time}.tgz"

    local(f"tar -czvf {out} {src}")
    return out


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.exists(archive_path):
        arch_file = archive_path[9:]
        new_version = "/data/web_static/releases/" + arch_file[:-4]
        arch_file = "/tmp/" + arch_file
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {new_version}")
        run(f"sudo tar -xzf {arch_file} -C {new_version}/")
        run(f"sudo rm {arch_file}")
        run(f"sudo mv {new_version}/web_static/* {new_version}")
        run(f"sudo rm -rf {new_version}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {new_version} /data/web_static/current")

        print("New version deployed!")
        return True

    return False


def deploy():
    """creates and distributes an archive to your web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except:
        return False
