import errors.e as er
import libs.commands as c
import os

def run(args):
    if(len(args) < 2): 
        dir = os.listdir()
        dir.sort()
        print('\t'.join(dir))
    else: 
        if (args[1] == "-h" or args[1] == "--help"):
            print("help")
        else:
            os.system("ls " + args[1])
        
        
