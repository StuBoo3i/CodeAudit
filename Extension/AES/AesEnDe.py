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


def decrypt_string(key, encrypted_data):
    # 对 Base64 编码的密文进行解码
    encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))

    # 提取 IV 和密文
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]

    # 创建 AES 解密器，并使用密钥和 IV 进行初始化
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # 进行解密，并去除填充
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # 返回解密后的明文
    plaintext = decrypted_data.decode('utf-8')
    return plaintext

if __name__ == '__main__':
    key = b'b7f97c7bae92cb66'  # 16 字节的密钥，需要根据实际情况进行替换
    plaintext = 'func'  # 要加密的明文

    encrypted_data = encrypt_string(key, plaintext)
    print(type(encrypted_data))
    print('加密后:', encrypted_data)

    decrypted_data = decrypt_string(key, encrypted_data)
    print('解密后:', decrypted_data)
