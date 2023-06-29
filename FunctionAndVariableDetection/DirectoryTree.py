import os
from Tools import Tree


def directory_tree(folder_path):
    """
    它将遍历项目文件夹的所有子文件夹和文件，并以目录树形式保存到树中。
    目录树使用了一些特殊的字符来表示文件夹和文件之间的层次关系。
    :param folder_path:项目根目录
    :return:目录树的根节点
    """
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
