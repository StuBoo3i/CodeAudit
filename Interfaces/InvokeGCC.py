import subprocess


def compile_code(source_file, output_file):
    command = ['gcc', source_file, '-o', output_file]
    subprocess.run(command)
    print("ok")
