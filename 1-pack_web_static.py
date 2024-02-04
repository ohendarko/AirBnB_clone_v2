#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder."""
from fabric.api import local
from datetime import datetime


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
