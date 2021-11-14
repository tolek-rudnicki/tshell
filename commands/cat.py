import errors.e as er
import libs.commands as c

def run(args):
    if(len(args) < 2):
        er.TooLittleArgsError("cat")
        pass
    else:
        f = open(args[1], "r+")
        print(f.read())
        f.close()