# 查找最长的哪一行数据
length_arr = []
max_line = 0 # 最长行数
max_length = 0 # 最大长度
max_line_txt = '' # 最长行
with open('test.sql', 'r', encoding='utf-8') as f:
    for i,line in enumerate(f.readlines()):
        if len(line) > max_length:
            max_length = len(line)
            max_line = i+1
            max_line_txt = line
print(max_line,max_length,max_line_txt)