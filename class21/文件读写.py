# 打开文件并读取内容
with open('class21/致橡树.txt', 'r') as file:
    lines = file.readlines()

# 删除所有包含 "作者：舒婷" 的行
lines = [line for line in lines if '作者：舒婷' not in line]

# 将修改后的内容写回文件
with open('class21/致橡树.txt', 'w') as file:
    file.writelines(lines)

with open('class21/致橡树.txt', 'r') as f:
    print(f.read())