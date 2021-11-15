import errors.e as er
import libs.commands as c

def run(args):
    if (len(args) > 1):
            if (c.commands.__contains__(args[1])):
                cmd_args = c.commands.get(args[1])
                clist = cmd_args.split(" ")
                for command in clist:
                    print("\t" + command)
            else:
                return er.UnknownCommandError(args[1])
    else:
        for i in c.commands:
            print(i)