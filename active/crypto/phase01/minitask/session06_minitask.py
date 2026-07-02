#!/usr/bin/env python3

import base64

plaintext = b"admin=true"
key = 0x23
cipher = bytes([x ^ key for x in plaintext])
hx = cipher.hex()
token = base64.b64encode(hx.encode())

print()
print("=== TASK1 ===")

print("plaintext    :", plaintext)
print("cipher       :", cipher)
print("cipher hex   :", hx)
print("token        :", token)

print()
print("=== TASK2 ===")

raw = base64.b64decode(token)

print("raw          :", raw)
print("type(raw)    :", type(raw))

print()
print("=== TASK3 ===")

cipher2 = bytes.fromhex(raw.decode())

print("cipher2      :", cipher2)
print("cipher2 hex  :", cipher2.hex())

print()
print("=== TASK4 ===")

token_decode = base64.b64decode(token)
hx_decode = bytes.fromhex(token_decode.decode())
recovered = bytes([x ^ key for x in hx_decode])

print("recovered    :", recovered)

print()
print("=== TASK5 ===")

samples = [b"68656c6c6f", b"aGVsbG8=", b"\x13\x37\xaa\xff"]

for s in samples:
    print(s)
