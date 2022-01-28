import libs.commands as c

def run(args):
    f = open("commands/" + args[1] + ".py", "w+")
    f.write("import os\nimport errors.e as er\nimport libs.commands as c\n\ndef run(args):\n    print(\"test\")")
    f.close()
    c.commands[args[1]] = args[2]
    print(args[1], args[2])
    #fi = open("libs/commands.py", "r")
    #content = fi.read()
    #fi.close()
    #fil = open("libs/commands.py", "w+")
    #content = content.replace("}", ''.join(args[2]) + "\n}")
    #fil.write("\"" + args[1] + "\": \"" + content +"\"")
    #fil.close()