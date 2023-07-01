import subprocess


def invoke_cppcheck(c_code_path):
    cppcheck_command = [r"E:\Data\Tools\Cppcheck\cppcheck.exe", "--platform=win64", "--enable=all",
                        "--inconclusive", c_code_path]
    result = subprocess.getoutput(cppcheck_command)
    return result
