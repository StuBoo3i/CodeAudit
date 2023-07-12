import json


class TreeNode:
    """
    树的定义类
    """
    def __init__(self, name):
        self.name = name
        self.children = []


def print_directory_tree(node, indent=''):
    """
    :param node: 输入树的节点名
    :param indent:
    :return: 在控制台打印输出树
    """
    print(indent + node.name)
    for child in node.children:
        print_directory_tree(child, indent + '|--')


def serialize_tree(node):
    """
    该函数使用递归方式将树转换为可以序列化的字典形式。它遍历节点和子节点，并为每个节点创建包含节点名称和子节点的字典。
    :param node: 输入树的节点
    :return: 树的序列化的字典形式
    """
    serialized = {
        "name": node.name,
        "children": []
    }

    for child in node.children:
        serialized_child = serialize_tree(child)
        serialized["children"].append(serialized_child)

    return serialized


def write_tree_to_file(tree, file_path):
    """
    该函数接受树和文件路径作为参数，并将树以JSON格式写入指定的文件中。它使用json.dump函数将序列化的目录树写入文件
    :param tree:树的节点
    :param file_path:要存入的文件路径
    :return:无
    """
    with open(file_path, "w") as file:
        serialized_tree = serialize_tree(tree)
        json.dump(serialized_tree, file, indent=4)


def deserialize_tree(serialized):
    """
    该函数使用递归方式将从文件中读取的树数据转换为树的数据结构。它遍历序列化数据中的节点和子节点，并根据数据创建对应的TreeNode对象。
    :param serialized:json字符串
    :return:树的根节点
    """
    node = TreeNode(serialized["name"])

    for serialized_child in serialized["children"]:
        child_node = deserialize_tree(serialized_child)
        node.children.append(child_node)

    return node


def read_tree_from_file(file_path):
    """
    该函数接受文件路径作为参数，并从指定文件中读取树数据。它使用json.load函数加载JSON数据，并将其传递给deserialize_tree函数以还原树结构。
    :param file_path:读取文件路径
    :return:树的根节点
    """
    with open(file_path, "r") as file:
        serialized_tree = json.load(file)
        tree = deserialize_tree(serialized_tree)
        return tree
