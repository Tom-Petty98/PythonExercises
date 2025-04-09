#simple functions to better understand python runtime
from os import path
import sys
from inspect import getfile, currentframe


# You cannot just import modules from parent directories instead you have to navigate into the parentdirectory before importing
currentdir = path.dirname(path.abspath(getfile(currentframe())))
parentdir = path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import runtest

runtest.print_hi()

def is_path_imported_from_os():
    func_name = "getfile"
    module_name = "inspect"
    return (
        func_name in globals()
        and callable(globals()[func_name])
        and globals()[func_name].__module__ == module_name
    ) or module_name in globals()

print("Is getfile imported from inspect:", is_path_imported_from_os())
print(__name__)

#print(dir(__builtins__))
#print(dir(list))
#print(dir(sys))