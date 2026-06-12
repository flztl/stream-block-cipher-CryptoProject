from pathlib import Path

Path("1KB.txt").write_bytes(b"A" * 1024)

Path("100KB.txt").write_bytes(b"A" * 102400)

Path("1MB.txt").write_bytes(b"A" * 1048576)

print("Files generated successfully.")
