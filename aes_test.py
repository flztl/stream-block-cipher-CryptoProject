from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'

plaintext = b'Confidential Message'

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(
    pad(plaintext, AES.block_size)
)

print("Ciphertext:", ciphertext.hex())

cipher_dec = AES.new(key, AES.MODE_ECB)

decrypted = unpad(
    cipher_dec.decrypt(ciphertext),
    AES.block_size
)

print("Decrypted:", decrypted.decode())
