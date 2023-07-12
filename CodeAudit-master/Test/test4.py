import re

str = "int a, int b, bool c, flout d"

# 使用正则表达式匹配参数
pattern = r"\b\w+\s\w+\b"
matches = re.findall(pattern, str)

# 将匹配到的参数存储到列表中
param_list = list(matches)

# 打印结果
print(param_list)
print(param_list.__len__())
