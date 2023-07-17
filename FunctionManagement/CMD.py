import subprocess

def run_cmd(command):
    try:
        # 执行命令并捕获输出
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        # 命令执行出错，输出错误信息
        return str(e.output)

if __name__ =='__main__':
    # 示例：执行 ipconfig 命令
    result = run_cmd("ipconfig")
    print(result)
