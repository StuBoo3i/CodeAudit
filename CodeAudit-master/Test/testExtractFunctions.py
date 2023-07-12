from Tools import RelativePath
from Tools import Tree
from FunctionAndVariableDetection.ExtractFunctions import process_c_files
from FunctionAndVariableDetection.DirectoryTree import directory_tree
from Tools.DatabaseOperation import SQL

# 提取自定义函数
# custom_functions = extract_functions(c_code)
# print("Custom Functions:")
# print(custom_functions)

if __name__ == "__main__":
    # 生成目录树
    directory_tree1 = directory_tree('C:/Users/MZS'
                                     '/PycharmProjects/CodeAudit')

    # 将目录树写入文件
    Tree.write_tree_to_file(directory_tree1, RelativePath.relative_path('File/directory_tree.json'))
    # 从文件中读取目录树
    directory_tree33 = Tree.read_tree_from_file(RelativePath.relative_path('File/directory_tree.json'))
    # 提取自定义函数和库函数
    functions = process_c_files(directory_tree33, 'C:/Users/MZS'
                                                  '/PycharmProjects/CodeAudit')

    # print("无效函数:")
    # print(functionInvalidDetection(directory_tree33, 'C:/Users/MZS'
    #                                                  '/PycharmProjects'))

    mysql = SQL()

    print("函数信息:")
    for function in functions:
        # print(function)
        # print()
        print(mysql.insert_scan_function(mysql.cnx, mysql.cursor, function))
    mysql.close_SQL(mysql.cursor, mysql.cnx)
