#!/usr/bin/env python3

import base64

plaintext = b"HELLO"
key = 0x23
nonce = 0x10

keystream = bytes([key ^ nonce for _ in plaintext])

print()
print("=== TASK1 ===")

print("plaintext    :", plaintext)
print("key          :", key)
print("nonce        :", nonce)
print("keystream    :", keystream)
print("keystream hex:", keystream.hex())

print()
print("=== TASK2 ===")

nonce2 = 0x20
keystream2 = bytes([key ^ nonce2 for _ in plaintext])

print("keystream1   :", keystream.hex())
print("keystream2   :", keystream2.hex())

print()
print("=== TASK3 ===")

cipher = bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])
cipher2 = bytes([plaintext[i] ^ keystream2[i] for i in range(len(plaintext))])

print("cipher       :", cipher)
print("cipher hex   :", cipher.hex())
print("cipher2 hex  :", cipher2.hex())

print()
print("=== TASK4 ===")

p1 = b"attack=now"
p2 = b"retreat=no"
same_keystream = bytes([key ^ nonce for _ in range(len(p1))])

c1 = bytes([p1[i] ^ same_keystream[i] for i in range(len(p1))])
c2 = bytes([p2[i] ^ same_keystream[i] for i in range(len(p2))])
x = bytes([c1[i] ^ c2[i] for i in range(len(c1))])

print("x            :", x)
print("x hex        :", x.hex())

print()
print("=== TASK5 ===")

token = base64.b64encode(cipher)

print("token        :", token)
print("plain text   :", token.decode())
