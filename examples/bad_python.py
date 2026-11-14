import subprocess

def BadName(too, many, args, for2, this, function, really):  # bad_naming + too_many_args
    print("debug")                                           # debug_print
    result = eval("1+1")                                     # dangerous_call
    subprocess.run("ls", shell=True)                         # shell_injection_risk
    return result + 42                                       # magic_number


class bad_class:                                             # bad_naming
    def method(self):
        pass
