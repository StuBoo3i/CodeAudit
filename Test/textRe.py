import re


def replace_comments(string):
    lines = string.split('\n')  # 按行分割字符串
    for i, line in enumerate(lines):
        if '//' in line:
            lines[i] = re.sub(r'//.*', '', line)  # 使用正则表达式替换注释部分为''
    new_string = '\n'.join(lines)  # 将处理后的行重新连接为字符串
    return new_string


# 测试代码
text = '''
int a = 5; // 变量赋值
int b = 10; // 另一个变量赋值
int c = a + b; // 计算结果
'''
new_text = replace_comments(text)
print(new_text)
