#!/usr/bin/env python3

import base64

print()
print("=== TASK1 ===")

text = "admin=true"
raw = text.encode()
token = base64.b64encode(raw)

print("text         :", text)
print("type(text)   :", type(text))
print("raw          :", raw)
print("type(raw)    :", type(raw))
print("token        :", token)
print("type(token)  :", type(token))

print()
print("=== TASK2 ===")

raw2 = base64.b64decode(token)
plain = raw2.decode()

print("raw          :", raw2)
print("type(raw)    :", type(raw2))
print("plain text   :", plain)
print("type(plain)  :", type(plain))

print()
print("=== TASK3 ===")

plaintext = b"admin=true"
key = 0x23
cipher = bytes([x ^ key for x in plaintext])
token2 = base64.b64encode(cipher)

print("plaintext    :", plaintext)
print("cipher       :", cipher)
print("token        :", token2)

print()
print("=== TASK4 ===")

raw3 = base64.b64decode(token2)
recovered = bytes([x ^ key for x in raw3])

print("raw          :", raw3)
print("recovered    :", recovered)

print()
print("=== TASK5 ===")

target = b"admin=false"
target_cipher = bytes([x ^ key for x in target])
target_token = base64.b64encode(target_cipher)

print("target       :", target)
print("token        :", target_token)
