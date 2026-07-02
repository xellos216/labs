#!/usr/bin/env python3

text = b"HELLO"
key = b"KEY"

print()
print("=== TASK1 ===")

print("plaintext    :", text)
print("key          :", key)

for i in range(len(text)):
    p = text[i]
    k = key[i % len(key)]
    print(i, chr(p), chr(k))

print()
print("=== TASK2 ===")

out = []

for i in range(len(text)):
    p = text[i]
    k = key[i % len(key)]
    c = p ^ k
    out.append(c)
    print(chr(p), "^", chr(k), "=", c)

cipher = bytes(out)

print("cipher       :", cipher)
print("cipher hex   :", cipher.hex())

print()
print("=== TASK3 ===")

plain = []

for i in range(len(cipher)):
    c = cipher[i]
    k = key[i % len(key)]
    p = c ^ k
    plain.append(p)
    print(c, "^", k, "=", p)

plain_bytes = bytes(plain)

print("recovered    :", plain_bytes)
print("plain text   :", plain_bytes.decode("ascii"))

print()
print("=== TASK4 ===")

cipher_hex = "030015070a"
cipher2 = bytes.fromhex(cipher_hex)

print("cipher2      :", cipher2)
print("cipher2 hex  :", cipher2.hex())

plain2 = bytes([
    cipher2[i] ^ key[i % len(key)]
    for i in range(len(cipher2))
])

print("recovered    :", plain2)
print("plain text   :", plain2.decode("ascii"))

print()
print("=== TASK5 ===")

plaintext = b"admin=true"
cipher3 = bytes([
    plaintext[i] ^ key[i % len(key)]
    for i in range(len(plaintext))
])
keystream = bytes([
    cipher3[i] ^ plaintext[i]
    for i in range(len(cipher3))
])

print("plaintext    :", plaintext)
print("cipher hex   :", cipher3.hex())
print("keystream    :", keystream)
print("keystream hex:", keystream.hex())
