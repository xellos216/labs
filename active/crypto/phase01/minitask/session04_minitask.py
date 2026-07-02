#!/usr/bin/env python3

plaintext = b"HELLO"
key = b"KEY"

cipher = bytes([plaintext[i] ^ key[i % len(key)] for i in range(len(plaintext))])

print()
print("=== TASK1 ===")

keystream = bytes([key[i % len(key)] for i in range(len(plaintext))])

print("plaintext    :", plaintext)
print("cipher hex   :", cipher.hex())
print("keystream    :", keystream)
print("plain text   :", keystream.decode())
print("stream list  :", list(keystream))
print("keystream hex:", keystream.hex())

print()
print("=== TASK2 ===")

recovered = bytes([plaintext[i] ^ cipher[i] for i in range(len(cipher))])

print("recovered    :", recovered)
print("plain text   :", recovered.decode())
print("stream list  :", list(recovered))
print("keystream hex:", recovered.hex())

print()
print("=== TASK3 ===")

plaintext2 = b"admin=true"
cipher2 = bytes([plaintext2[i] ^ key[i % len(key)] for i in range(len(plaintext2))])
keystream2 = bytes([plaintext2[i] ^ cipher2[i] for i in range(len(plaintext2))])

print("cipher2 hex  :", cipher2.hex())
print("keystream    :", keystream2)
print("stream list  :", list(keystream2))
print("keystream hex:", keystream2.hex())

print()
print("=== TASK4 ===")

known = b"admin="
partial = bytes([cipher2[i] ^ known[i] for i in range(len(known))])

print("known        :", known)
print("partial      :", partial)
print("stream list  :", list(partial))
print("partial hex  :", partial.hex())

print()
print("=== TASK5 ===")

p1 = b"attack=now"
p2 = b"retreat=no"

c1 = bytes([p1[i] ^ key[i % len(key)] for i in range(len(p1))])
c2 = bytes([p2[i] ^ key[i % len(key)] for i in range(len(p2))])
x = bytes([c1[i] ^ c2[i] for i in range(len(c1))])

print("x            :", x)
print("c1 hex       :", c1.hex())
print("c2 hex       :", c2.hex())
print("x hex        :", x.hex())
