#!/usr/bin/env python3

import base64

print()
print("=== STEP1 ===")

x = b"68656c6c6f"
y = x.decode()

print(f"{x = }")
print(f"{type(x) = }")
print(f"{y = }")
print(f"{type(y) = }")

print()
print("=== STEP2 ===")

z = bytes.fromhex(y)

print(f"{z = }")
print(f"{type(z) = }")

print()
print("=== STEP3 ===")

x2 = b"414243"

print(f"{x2 = }")
print(f"{x2.decode() = }")
print(f"{bytes.fromhex(x2.decode()) = }")
print(f"{bytes.fromhex(x2.decode()).decode() = }")

print()
print("=== STEP4 ===")

A = b"414243"
B = "414243"
C = b"ABC"
D = bytes.fromhex("414243")
E = "ABC"

print(f"{A =}")
print(f"{B =}")
print(f"{C =}")
print(f"{D =}")
print(f"{E =}")

print()
print("=== STEP5 ===")

plain_text = "imhomgmin"
pt_encode = plain_text.encode()
key = 0x40

xor = bytes([x ^ key for x in pt_encode])

xor_hex = xor.hex()
xor_hex_encode = xor_hex.encode()
xor_hex_encode_base64 = base64.b64encode(xor_hex_encode)
token = xor_hex_encode_base64.decode()

print(f"{plain_text = }")
print(f"{pt_encode = }")
print(f"{xor = }")
print(f"{xor_hex = }")
print(f"{xor_hex_encode = }")
print(f"{xor_hex_encode_base64 = }")
print(f"{token = }")

print()
print("=== Mini Task ===")

mini_task = b"hello"

a = mini_task.hex()
b = a.encode()
c = base64.b64encode(b)

print(f"{mini_task = }")
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
print()
