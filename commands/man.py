import os
import errors.e as er

def run(args):
    if (len(args) == 2):
        os.system("man " + args[1])
    elif (len(args) > 2):
        er.TooManyArgsError(args[0])
    else:
        er.TooLittleArgsError(args[0])
