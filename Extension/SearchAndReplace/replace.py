def replace_string_in_file(file_path, original_string, replacement_string):
    # 读取文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 替换字符串
    replaced_content = content.replace(original_string, replacement_string)

    # 将替换后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(replaced_content)

if __name__ == "__main__":
    # 示例使用
    file_path = '../../File'
    original_string = 'fuc'
    replacement_string = 'function'
    replace_string_in_file(file_path, original_string, replacement_string)
