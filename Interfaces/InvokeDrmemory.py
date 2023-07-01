import subprocess


def invoke_drmemory(program_path):
    command = ['drmemory', '-batch', '-show_reachable', '--', program_path]
    output = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return output.decode('utf-8')


