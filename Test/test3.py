from LeakDetection.LeakDetection import leak_detection
from Interfaces.FromCToDll import compile_c_code
from Tools.RelativePath import relative_path

if __name__ == '__main__':
    # 设置输入和输出文件路径
    source_file = "File/example.c"  # C源文件路径
    output_file = "File/example.dll"  # 生成的动态链接库文件路径

    # 编译C代码
    compile_c_code(relative_path(source_file), relative_path(output_file))
    leak_detection(output_file)
