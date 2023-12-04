from Crypto.Cipher import Blowfish
from Crypto import Random

class BlowfishCipher:
    def _init_(self, key):
        self.key = key
        self.block_size = Blowfish.block_size
        self.cipher = None

    def pad(self, data):
        padding = self.block_size - len(data) % self.block_size
        return data + bytes([padding] * padding)

    def unpad(self, data):
        padding = data[-1]
        return data[:-padding]

    def encrypt(self, plaintext):
        plaintext = self.pad(plaintext)
        iv = Random.new().read(self.block_size)
        self.cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, bytes(iv))  # Convert iv to bytes
        ciphertext = iv + self.cipher.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:self.block_size]
        self.cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, bytes(iv))  # Convert iv to bytes
        plaintext = self.cipher.decrypt(ciphertext[self.block_size:])
        return self.unpad(plaintext)

if __name__ == "__main__":
    # Replace 'your_secret_key' with your actual secret key
    secret_key = b'your_secret_key'
    Cipher = BlowfishCipher(secret_key)

    plaintext = b'Hello, Blowfish!'
    print(f"Original Text: {plaintext.decode('utf-8')}")

    encrypted_text = Cipher.encrypt(plaintext)
    print(f"Encrypted Text: {encrypted_text.hex()}")

    decrypted_text = Cipher.decrypt(encrypted_text)
    print(f"Decrypted Text: {decrypted_text.decode('utf-8')}")