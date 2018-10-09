import os
import sys

# list all include paths and cpp files
def list_all_files(rootdir, includeArray, cppArray):
    includeArray.append(rootdir)

    list = os.listdir(rootdir)
    for _, value in enumerate(list):
        path = os.path.join(rootdir, value)
        if os.path.isdir(path) and not path.startswith("."):
            list_all_files(path, includeArray, cppArray)
        elif os.path.isfile(path) and path.endswith(".cpp"):
            cppArray.append(path)

PROJECT_ROOT = os.getcwd()
PROJECT_ROOT = eval(repr(PROJECT_ROOT).replace('\\\\', '/'))
SRC_DIR = PROJECT_ROOT + "/src"

includeArray = []
cppArray = []
list_all_files(SRC_DIR, includeArray, cppArray)

# concat include string
includeStr = ""
for index,value in enumerate(includeArray):
    includeStr += " -I " + value + " "

includeStr = eval(repr(includeStr).replace('\\\\', '/'))

# concat cpp string
cppStr = ""
for index,value in enumerate(cppArray):
    cppStr += " " + value + " "

cppStr = eval(repr(cppStr).replace('\\\\', '/'))

# compile
print("Begin compiling with 'g++ -g -std=c++11'")

print("\nPROJECT_ROOT: " + PROJECT_ROOT)
print("SRC_DIR: " + SRC_DIR)

cmd = ""
for i in range(len(sys.argv) - 1):
    cmd += sys.argv[i + 1]

cmd += includeStr
cmd += cppStr
print("\ncompile command: " + cmd)

result = os.system(cmd)
if result == 0:
    print("\ncompile successfully")
else:
    print("\n>>>>>>>compile failed")

print("\nEnd compiling")