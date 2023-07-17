from Interfaces.InvokeGCC import compile_code
from Interfaces.InvokeDrmemory import invoke_drmemory, translate
from Tools.RelativePath import relative_path
if __name__ == '__main__':
    # 设置输入和输出文件路径
    source_file = "File/test.c"  # C源文件路径
    output_file = "File/test"  # 生成的文件路径

    Static_leak_detection(source_file)
