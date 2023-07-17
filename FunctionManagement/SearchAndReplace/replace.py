import os
def replace_string_in_file(file_path, original_string, replacement_string):
    # 读取文件内容
    with open(file_path, 'r') as file:
        content = file.read()

    # 替换字符串
    replaced_content = content.replace(original_string, replacement_string)

    # 将替换后的内容写回文件
    with open(file_path, 'w') as file:
        file.write(replaced_content)


def replace_keywords_in_project(project_path, original_keyword, replacement_keyword):
    # 遍历项目目录中的所有文件和文件夹
    for root, dirs, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)

            # 只处理文本文件，可以根据需要进行修改
            if file_path.endswith('.c') or file_path.endswith('.h'):
                # 读取文件内容
                with open(file_path, 'r') as f:
                    content = f.read()

                # 替换关键字
                replaced_content = content.replace(original_keyword, replacement_keyword)

                # 将替换后的内容写回文件
                with open(file_path, 'w') as f:
                    f.write(replaced_content)

    print("关键字替换完成。")
if __name__ == "__main__":
    # 示例使用
    file_path = '../../File'
    original_string = 'fuc'
    replacement_string = 'function'
    replace_string_in_file(file_path, original_string, replacement_string)
