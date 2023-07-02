"""
项目文件的相对路径
"""
import os


def relative_path(path):
    """
    输入以本项目为根目录的文件路径返回绝对路径
    :param path: 输入以本项目为根目录的文件路径
    :return: 返回本地绝对路径
    """
    return os.path.join(os.path.dirname(os.getcwd()), path)


def s_relative_path():
    """
    输入以本项目为根目录的文件路径返回绝对路径
    :param path: 输入以本项目为根目录的文件路径
    :return: 返回本地绝对路径
    """
    return os.path.dirname(os.getcwd())
