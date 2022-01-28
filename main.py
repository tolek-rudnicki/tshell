import tparser
import getpass
import platform
import os
import sys
from libs.colors import *
import win32.main as win

while (True):
    path = os.getcwd()
    home = os.path.expanduser('~')
    if sys.platform == "win32":
        cmd = input(path + ">")
        win.parse(cmd)
    else:
        if path.startswith(home):
            path = path.replace(home, '~', 1)
        cmd = input(Colors.LIGHT_GREEN + getpass.getuser() + "@" + platform.node() + Colors.WHITE + ":" + Colors.LIGHT_BLUE + path + Colors.WHITE + "$ ")
        tparser.parse(cmd)