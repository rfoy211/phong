import os
src = 'D:\\python1\\phong\\a\\a.txt'

if os.path.exists(src):
    print("file existed")
    if os.path.isfile(src):
        print("this is a file")
    elif os.path.isdir(src):
        print("this is a directory")
else:
    print("this location doesn't exist")