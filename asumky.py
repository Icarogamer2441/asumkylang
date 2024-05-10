variables = {}
functions = {}
commands = {}

def funcinterpret(code):
    lines = code.split("\n")

    for linne in lines:
        if linne.startswith("push"):
            pushtype = linne.split(" ")[1].strip("\"\'")
            if pushtype.startswith("prc"):
                char = linne.split(", ")[1].strip("\"\'")
                if char == "newline":
                    print("")
                else:
                    if len(char) > 1:
                        print("an char can have only 1 character")
                    elif len(char) < 1:
                        print("an char need to have 1 character")
                    else:
                        print(char, end="")
            elif pushtype.startswith("prv"):
                varname = linne.split(", ")[1].strip("\"\'")
                print(variables.get(varname), end="")
        elif linne.startswith("set"):
            settype = linne.split(" ")[1].strip("\"\'")
            if settype.startswith("int"):
                varname = linne.split("> ")[1].split(", ")[0].strip("\"\'")
                value = linne.split(", ")[1].strip("\"\'")
                variables[varname] = int(value)
            elif settype.startswith("string"):
                varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                value = linne.split(", >")[1].split("<")[0].strip("\"\'")
                variables[varname] = value
            elif settype.startswith("input"):
                varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                inputmsg = linne.split(", >")[1].split("<")[0].strip("\"\'")
                variables[varname] = input(inputmsg)
        elif linne.startswith("call"):
            funcname = linne.split(", ")[1].strip("\"\'")
            funccode = "\n".join(functions[funcname])
            interpret(funccode)

def interpret(code):
    lines = code.split("\n")

    for line in lines:
        if line.startswith("start:"):
            for linne in lines:
                if linne.startswith("push"):
                    pushtype = linne.split(" ")[1].strip("\"\'")
                    if pushtype.startswith("prc"):
                        char = linne.split(", ")[1].strip("\"\'")
                        if char == "newline":
                            print("")
                        else:
                            if len(char) > 1:
                                print("an char can have only 1 character")
                            elif len(char) < 1:
                                print("an char need to have 1 character")
                            else:
                                print(char, end="")
                    elif pushtype.startswith("prv"):
                        varname = linne.split(", ")[1].strip("\"\'")
                        print(variables.get(varname), end="")
                elif linne.startswith("set"):
                    settype = linne.split(" ")[1].strip("\"\'")
                    if settype.startswith("int"):
                        varname = linne.split("> ")[1].split(", ")[0].strip("\"\'")
                        value = linne.split(", ")[1].strip("\"\'")
                        variables[varname] = int(value)
                    elif settype.startswith("string"):
                        varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                        value = linne.split(", >")[1].split("<")[0].strip("\"\'")
                        variables[varname] = value
                    elif settype.startswith("input"):
                        varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                        inputmsg = linne.split(", >")[1].split("<")[0].strip("\"\'")
                        variables[varname] = input(inputmsg)
                elif linne.startswith("call"):
                    funcname = linne.split(", ")[1].strip("\"\'")
                    funccode = "\n".join(functions[funcname])
                    funcinterpret(funccode)
        elif line.startswith("data:"):
            continuecode = False
            for linne in lines:
                if linne.startswith("data:"):
                    continuecode = True
                elif linne == "":
                    continuecode = False
                    break
                if continuecode:
                    if linne.startswith("define"):
                        definetype = linne.split(" ")[1].strip("\"\'")
                        if definetype.startswith("func"):
                            funcname = linne.split(", ")[1].strip("\"\'")
                            functions[funcname] = []
                    elif linne.startswith("set"):
                        settype = linne.split(" ")[1].strip("\"\'")
                        if settype.startswith("int"):
                            varname = linne.split("> ")[1].split(", ")[0].strip("\"\'")
                            value = linne.split(", ")[1].strip("\"\'")
                            variables[varname] = int(value)
                        elif settype.startswith("string"):
                            varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                            value = linne.split(", >")[1].split("<")[0].strip("\"\'")
                            variables[varname] = value
                        elif settype.startswith("input"):
                            varname = linne.split("> ")[1].split(", >")[0].strip("\"\'")
                            inputmsg = linne.split(", >")[1].split("<")[0].strip("\"\'")
                            variables[varname] = input(inputmsg)
        for func in functions:
            continuecode = False
            if line.startswith(func + ":"):
                for linne in lines:
                    if linne.startswith(f"{func}:"):
                        continuecode = True
                    elif linne == "":
                        continuecode = False
                        break
                    if continuecode:
                        codee = linne
                        functions[func].append(codee)

def execute_file(filename):
    if filename.endswith(".asu"):
        with open(filename, "r") as f:
            interpret(f.read())
    elif filename.endswith(".asum"):
        with open(filename, "r") as f:
            interpret(f.read())
    else:
        print("use a .asu or .asum file extension")

file = input("what's your .asu or .asum file? > ")
execute_file(file)
