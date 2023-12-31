from Tools import RelativePath
from Tools import Tree
from FunctionAndVariableDetection.DirectoryTree import directory_tree

if __name__ == "__main__":

    # 生成目录树
    directory_tree1 = directory_tree('D:/Software/Engine')

    # 将目录树写入文件
    Tree.write_tree_to_file(directory_tree1, RelativePath.relative_path('File/directory_tree.json'))

    # 从文件中读取目录树
    directory_tree33 = Tree.read_tree_from_file(RelativePath.relative_path('File/directory_tree.json'))

    # 打印目录树
    Tree.print_directory_tree(directory_tree33)
