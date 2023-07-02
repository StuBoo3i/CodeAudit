from Tools import RelativePath
from Tools import Tree
from FunctionAndVariableDetection.ExtractFunctions import process_c_files
from InvalidFunctionDetection.FunctionInvalidDetection import functionInvalidDetection

# 提取自定义函数
# custom_functions = extract_functions(c_code)
# print("Custom Functions:")
# print(custom_functions)

if __name__ == "__main__":
    # 从文件中读取目录树
    directory_tree33 = Tree.read_tree_from_file(RelativePath.relative_path('File/directory_tree.json'))
    # 提取自定义函数和库函数
    functions = process_c_files(directory_tree33, 'C:/Users/MZS'
                                                  '/PycharmProjects')

    # print("无效函数:")
    # print(functionInvalidDetection(directory_tree33, 'C:/Users/MZS'
    #                                                  '/PycharmProjects'))

    print("函数信息:")
    for function in functions:
        print("返回类型:", function['return_type'])
        print("函数名:", function['function_name'])
        print("参数列表:", function['parameters'])
        print("函数体:")
        print(function['body'])
        print("路径:", function['path'])
        print("起:", function['start'])
        print("止:", function['end'])
        print()
