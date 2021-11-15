def UnknownCommandError(command):
        print("Unknown command '" + command + "'")
def TooLittleArgsError(command):
        print("Too few arguments for '" + command + "'")
def TooManyArgsError(command):
        print("To many arguments for '" + command + "'")
def UnknownArgumentError(command, atr):
        print("The command " + command + "has no attribute " + atr)