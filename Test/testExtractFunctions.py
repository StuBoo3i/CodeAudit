from Tools import RelativePath
from Tools import Tree
from FunctionAndVariableDetection.extractFunctions import process_c_files

# 提取自定义函数
# custom_functions = extract_functions(c_code)
# print("Custom Functions:")
# print(custom_functions)

if __name__ == "__main__":
    # 从文件中读取目录树
    directory_tree33 = Tree.read_tree_from_file(RelativePath.relative_path('File/directory_tree.json'))
    # 提取自定义函数和库函数
    custom_functions, library_functions = process_c_files(directory_tree33, 'C:/Users/MZS'
                                                                                              '/PycharmProjects')

    print("Custom Functions:")
    print(custom_functions)

    print("Library Functions:")
    print(library_functions)

    Tree.print_directory_tree(directory_tree33)
