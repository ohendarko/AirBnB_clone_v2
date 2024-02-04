#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
"""Fabric script that generates a .tgz archive"""


@task
def do_pack(c):
    """
    Function that Generates a .tgz archive
    """
    local("mkdir -p versions")
    src = "web_static/"
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    out = f"versions/web_static_{time}.tgz"

    c.local(f"tar -czvf {out} {src}")
    return out
