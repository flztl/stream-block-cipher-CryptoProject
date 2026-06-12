import time
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# =========================
# RC4 CLASS
# =========================

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


# =========================
# RC4 PERFORMANCE
# =========================

def measure_rc4(file_path, key="Secret123"):

    data = Path(file_path).read_bytes()

    rc4 = RC4(key)

    start = time.perf_counter()
    encrypted = rc4.encrypt(data)
    enc_time = time.perf_counter() - start

    rc4 = RC4(key)

    start = time.perf_counter()
    rc4.decrypt(encrypted)
    dec_time = time.perf_counter() - start

    return enc_time, dec_time


# =========================
# AES PERFORMANCE
# =========================

def measure_aes(file_path):

    data = Path(file_path).read_bytes()

    key = b'1234567890123456'

    cipher = AES.new(key, AES.MODE_ECB)

    start = time.perf_counter()

    encrypted = cipher.encrypt(
        pad(data, AES.block_size)
    )

    enc_time = time.perf_counter() - start

    cipher = AES.new(key, AES.MODE_ECB)

    start = time.perf_counter()

    unpad(
        cipher.decrypt(encrypted),
        AES.block_size
    )

    dec_time = time.perf_counter() - start

    return enc_time, dec_time


# =========================
# RUN TEST
# =========================

files = [
    "1KB.txt",
    "100KB.txt",
    "1MB.txt"
]

for file in files:

    rc4_enc, rc4_dec = measure_rc4(file)
    aes_enc, aes_dec = measure_aes(file)

    print("\nFILE:", file)

    print("RC4 Encrypt :", round(rc4_enc * 1000, 3), "ms")
    print("RC4 Decrypt :", round(rc4_dec * 1000, 3), "ms")

    print("AES Encrypt :", round(aes_enc * 1000, 3), "ms")
    print("AES Decrypt :", round(aes_dec * 1000, 3), "ms")
