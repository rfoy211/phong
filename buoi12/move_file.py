import os

scr = "D:\\python1\\phong\\buoi12\\file_detection.py"
dst = "D:\\python1\\phong\\buoi12\\"

try:
    if os.path.exists(dst):
        print("there is already a file there")
    else:
        os.replace(src, "was moved")
        print(src , "was moved")
except FileNotFoundError:
    print(src, "was not found")

scr = "D:\\python1\\phong\\buoi12\\file_detection.py"
dst = "D:\\python1\\phong\\buoi12\\"
try:
    if os.path.exists(dst):
        print("there is already a file there")
    else:
        os.replace(src, "was moved")
        print(src , "was moved")
except FileNotFoundError:
    print(src, "was not found")