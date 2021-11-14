import errors.e as er
import libs.commands as c

def run(args):
    if(len(args) < 2):
        # throw no args error
        pass
    else:
        f = open(args[1], "r+")
        print(f.read())
        f.close()