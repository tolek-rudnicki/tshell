import errors.e as er
import libs.commands as c

def run(args):
    if (len(args) > 1):
            if (c.commands.__contains__(args[1])):
                cmd_args = c.commands.get(args[1])
                clist = cmd_args.split(" ")
                for i in clist:
                    print("         " + i)
            else:
                return er.UnknownCommandError(args[1])
    else:
        print("help [command] - shows this menu or shows arguments of given command")