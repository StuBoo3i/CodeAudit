import subprocess


# 编译C代码并生成动态链接库文件
def compile_c_code(source_file, output_file):
    command = f"gcc -shared -o {output_file} {source_file}"
    subprocess.run(command, shell=True)
