import os
import errors.e as er
import libs.variables as vars

def run(args):
    if (args[1] == "woman"):
        if (vars.unlocked == True):
            os.system("man " + args[1])
        else:
            print("You have not unlocked this command do 'unlock wrjks' the password is 'wrjks' to unlock it!")
    else:
        if (len(args) == 2):
            os.system("man " + args[1])
        elif (len(args) > 2):
            er.TooManyArgsError(args[0])
        else:
            er.TooLittleArgsError(args[0])
