import shutil
src = "D:\\python1\\phong\\buoi12\\file_detection.py"
dst = "D:\\python1\\phong\\buoi12\\"
shutil.copyfile (src, dst + 'test_copyfile.txt')
shutil.copy(src, dst + 'test_copy.txt')
shutil.copy2(src, dst + 'test_copy2.txt')