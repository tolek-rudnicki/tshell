import errors.e as er
import libs.commands as c
import os

def run(args):
    if(len(args) > 2):
        er.TooManyArgsError(args[0])
    elif (len(args) == 2):
        #os.system("cd " + args[1])
        os.chdir(args[1])
    else:
        er.TooLittleArgsError(args[0])