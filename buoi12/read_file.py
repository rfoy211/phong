src = "D:\\python1\\phong\\a\\a.txt"
text = ['hello world\n\hello world\n\hello world\n\hello world\n']
text2 = 'hi hi hi'

# đọc file báo lỗi
with open(src, 'r') as file:
    file.read()

# with open(scr2, 'r') as file:
#     file.read()
# w xóa nội dung
with open(src, 'x') as file:
    file.write(text)
# a thêm nội dung
with open(src, 'w') as file:
    file.write(text2)

print(file.closed)