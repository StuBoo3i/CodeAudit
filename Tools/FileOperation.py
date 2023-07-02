def write_to_file(path, string):
    """
    将一个字符串读入文件
    :param path: 文件路径
    :param string: 读入字符串
    :return: 无
    """
    with open(path, 'w') as file:
        file.write(string)


def print_lines(path, string):
    """
    在文件中匹配字符串
    :param path: 需阅读文件
    :param string: 匹配字符串
    :return: 匹配字符串所在整行的list
    """
    lines = []
    with open(path, 'r') as file:
        for line in file:
            if string in line:
                lines.append(line.strip())
    return lines
