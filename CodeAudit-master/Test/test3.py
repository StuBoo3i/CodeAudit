from LeakDetection.LeakDetection import Static_leak_detection
from Interfaces.InvokeGCC import compile_code

if __name__ == '__main__':
    # 设置输入和输出文件路径
    source_file = "File/example.c"  # C源文件路径
    output_file = "File/example.exe"  # 生成的文件路径

    Static_leak_detection(source_file)
