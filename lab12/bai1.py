file_path = 'D:\\python1\\phong\\buoi12\\read_file.py'

with open(file_path, 'r') as file:
    list_name = [('-' +item.replace('\n', '')) for item in file.readlines()]
    for i in list_name:
        print(i)