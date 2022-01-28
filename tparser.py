import errors.e as er

import commands.help as help
import commands.cat as cat
import commands.ls as ls
import commands.clear as clear
import commands.cd as cd
import commands.unlock as unlock
import commands.man as man
import commands.make as make
import commands.lolcat as lolcat

import libs.commands as c

def parse(command):
    args = command.split(" ")
    cmd = args[0]
    if (cmd == "help"):
        help.run(args)
    elif (cmd == "cat"):
        cat.run(args)
    elif (cmd == "ls"):
        ls.run(args)
    elif (cmd == "clear"):
        clear.run()
    elif (cmd == "cd"):
        cd.run(args)
    elif (cmd == "clear"):
        clear.run()
    elif (cmd == "unlock"):
        unlock.run(args)
    elif (cmd == "man"):
        man.run(args)
    elif (cmd == "make"):
        make.run(args)
    elif (cmd == "lolcat"):
        lolcat.run(args)
    else:
        return er.UnknownCommandError(cmd)