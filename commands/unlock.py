import errors.e as er
import libs.variables as vars

def run(args):
    if(len(args) == 2):
        if (args[1] == "wrjks"):
            passwd = input("Enter password: ")
            if (passwd == "wrjks"):
                vars.unlocked = True
                print("Weird jokes are now unlocked")
                print("Type 'man woman' to console and see what happens")
            else:
                print("Wrong password")
        else:
            er.UnknownArgumentError(args[0], args[1])
    elif (len(args) > 2):
        er.TooManyArgsError(args[0])
    else:
        er.TooLittleArgsError(args[0])
