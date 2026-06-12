import time

class RC4:
    def __init__(self, key):
        self.S = list(range(256))
        self.key = [ord(c) for c in key]
        self.ksa()

    def ksa(self):
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def prga(self):
        S = self.S.copy()
        i = j = 0

        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256

            S[i], S[j] = S[j], S[i]

            K = S[(S[i] + S[j]) % 256]
            yield K

    def encrypt(self, plaintext):
        keystream = self.prga()
        return bytes([b ^ next(keystream) for b in plaintext])

    def decrypt(self, ciphertext):
        keystream = self.prga()
        return bytes([b ^ next(keystream) for b in ciphertext])


# Example Usage

key = "Secret123"
plaintext = b"HELLO WORLD"

rc4 = RC4(key)

ciphertext = rc4.encrypt(plaintext)
print("Ciphertext:", ciphertext.hex())

rc4_dec = RC4(key)
decrypted = rc4_dec.decrypt(ciphertext)

print("Decrypted:", decrypted.decode())
