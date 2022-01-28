import errors.e as er
import libs.commands as c

def run(args):
    try:
        if(len(args) < 2):
            er.TooLittleArgsError("cat")
            pass
        else:
            f = open(args[1], "r+")
            print(f.read())
            f.close()
    except FileNotFoundError as e:
        e = str(e).split("]")[1]
        print(e)