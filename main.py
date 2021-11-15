import tparser
import getpass
import platform
import os
from libs.colors import *
import libs.variables as vars

while (True):
    path = os.getcwd()
    home = os.path.expanduser('~')
    if path.startswith(home):
        path = path.replace(home, '~', 1)
    cmd = input(Colors.LIGHT_GREEN + getpass.getuser() + "@" + platform.node() + Colors.WHITE + ":" + Colors.LIGHT_BLUE + path + Colors.WHITE + "$ ")
    tparser.parse(cmd)