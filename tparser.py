import errors.e as er
import commands.help as help
import commands.cat as cat
import libs.commands as c

def parse(command):
    args = command.split(" ")
    cmd = args[0]
    if (cmd == "help"):
        help.run(args)
    elif (cmd == "test"):
        if(len(args) < 2): 
            print("test") 
        else: 
            print("test123")
    elif (cmd == "cat"):
        cat.run(args)
    else:
        return er.UnknownCommandError(cmd)