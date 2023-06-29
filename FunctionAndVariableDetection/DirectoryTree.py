import os
from Tools import Tree


def directory_tree(folder_path):
    node = Tree.TreeNode(os.path.basename(folder_path))

    files = os.listdir(folder_path)
    files.sort()  # 可选，按照名称排序文件和文件夹

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # 判断是否是文件夹
        if os.path.isdir(file_path):
            subfolder_path = os.path.join(folder_path, file_name)
            child_node = directory_tree(subfolder_path)
            node.children.append(child_node)
        else:
            child_node = Tree.TreeNode(file_name)
            node.children.append(child_node)

    return node
