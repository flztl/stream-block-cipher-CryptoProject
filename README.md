# stream-block-cipher-CryptoProject

## Overview
This project implements and evaluates two symmetric cryptographic algorithms:

- RC4-like Stream Cipher
- AES Block Cipher

The project compares both algorithms in terms of security and performance using files of different sizes (1 KB, 100 KB, and 1 MB).

## Requirements

Install PyCryptodome:

```bash
pip install pycryptodome
```

## Files

- `rc4_test.py` - RC4-like encryption and decryption
- `aes_test.py` - AES-128 encryption and decryption
- `generate_files.py` - Generate test files
- `performance_test.py` - Performance testing

## How to Run

Generate test files:

```bash
python generate_files.py
```

Run RC4 test:

```bash
python rc4_test.py
```

Run AES test:

```bash
python aes_test.py
```

Run performance test:

```bash
python performance_test.py
```

## Conclusion

- RC4-like provides faster encryption and decryption.
- AES provides stronger security and is the recommended algorithm for secure file storage.
- AES is the overall recommended algorithm due to its security and practical performance.
