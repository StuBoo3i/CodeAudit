from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os


def encrypt_file(key, input_file, output_file):
    # 生成一个随机的初始化向量（IV）
    iv = get_random_bytes(AES.block_size)

    # 创建 AES 加密器，并使用密钥和 IV 进行初始化
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 打开输入文件和输出文件
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            # 写入 IV 到输出文件
            f_out.write(iv)

            while True:
                # 逐块读取文件内容
                chunk = f_in.read(1024)
                if len(chunk) == 0:
                    break

                # 对块进行填充，并进行加密
                encrypted_chunk = cipher.encrypt(pad(chunk, AES.block_size))

                # 写入加密后的数据到输出文件
                f_out.write(encrypted_chunk)


def decrypt_file(key, input_file, output_file):
    # 打开输入文件和输出文件
    with open(input_file, 'rb') as f_in:
        # 读取 IV
        iv = f_in.read(AES.block_size)

        # 创建 AES 解密器，并使用密钥和 IV 进行初始化
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(output_file, 'wb') as f_out:
            while True:
                # 逐块读取加密后的数据
                encrypted_chunk = f_in.read(1024)
                if len(encrypted_chunk) == 0:
                    break

                # 解密并去除填充
                decrypted_chunk = unpad(cipher.decrypt(encrypted_chunk), AES.block_size)

                # 写入解密后的数据到输出文件
                f_out.write(decrypted_chunk)


def encrypt_string(key, plaintext):
    # 生成一个随机的初始化向量（IV）
    iv = get_random_bytes(AES.block_size)

    # 创建 AES 加密器，并使用密钥和 IV 进行初始化
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 对明文进行填充，并进行加密
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    # 将 IV 和密文进行合并，并进行 Base64 编码
    encrypted_data = base64.b64encode(iv + ciphertext).decode('utf-8')
    return encrypted_data


from Crypto.Cipher import AES
import base64


def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]


def decrypt_string(key, encrypted_data):
    # 对 Base64 编码的数据进行解码
    decoded_data = base64.b64decode(encrypted_data)

    # 提取 IV 和密文
    iv = decoded_data[:AES.block_size]
    ciphertext = decoded_data[AES.block_size:]

    # 创建 AES 解密器，并使用密钥和 IV 进行初始化
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 进行解密，并移除填充
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)

    # 解码为字符串
    plaintext = plaintext.decode('latin-1')

    return plaintext

from Extension.HashFunction import SHA
if __name__ == '__main__':
    key = SHA.generate_sha_digest("mypasswprd")[:16].encode()  # 16 字节的密钥，需要根据实际情况进行替换
    encrypted_data = 'XfMyikaEuzn+aKr0Ed5IfOkNb7eShogJjcWyZRO0q8TGmwmWabyeOwg+bRKNsuJjUp7++NW/zEOXtK/HR+t39Ql1ahAQATjVaUnzPe0mZWc='  # 要加密的明文

    #encrypted_data = encrypt_string(key, plaintext)
    print('加密后:', encrypted_data)

    decrypted_data = decrypt_string(key, encrypted_data)
    print('解密后:', decrypted_data)
