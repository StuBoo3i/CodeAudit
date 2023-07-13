from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
def encrypt_file(public_key_str, input_file, output_file):
    public_key = RSA.import_key(public_key_str)
    cipher = PKCS1_OAEP.new(public_key)

    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                chunk = f_in.read(214)
                if len(chunk) == 0:
                    break
                ciphertext = cipher.encrypt(chunk)
                f_out.write(ciphertext)

def decrypt_file(private_key_str, input_file, output_file):
    private_key = RSA.import_key(private_key_str)
    cipher = PKCS1_OAEP.new(private_key)

    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                chunk = f_in.read(256)
                if len(chunk) == 0:
                    break
                plaintext = cipher.decrypt(chunk)
                f_out.write(plaintext)

def encrypt_string(public_key_str, plaintext):
    public_key = RSA.import_key(public_key_str)
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    encrypted_data = base64.b64encode(ciphertext).decode('utf-8')
    return encrypted_data

def decrypt_string(private_key_str, encrypted_data):
    private_key = RSA.import_key(private_key_str)
    cipher = PKCS1_OAEP.new(private_key)
    ciphertext = base64.b64decode(encrypted_data)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext

def generate_rsa_key_pair(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key





if __name__ == '__main__':
    private_key, public_key = generate_rsa_key_pair()
    print('私钥:', private_key.decode('utf-8'))
    print('公钥:', public_key.decode('utf-8'))
