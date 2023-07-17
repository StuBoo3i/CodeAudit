import hashlib

def generate_sha_digest(string):
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    digest = sha256.hexdigest()
    return digest


if __name__ == "__main__":
    # Example usage
    string = "mypasswprd"
    digest = generate_sha_digest(string)
    print("String:", string)
    print("SHA Digest:", digest)



'''
账号名: admin
密码：mypassword
'''