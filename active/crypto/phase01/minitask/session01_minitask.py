#!/usr/bin/env python3

text = "ABC"
raw = text.encode()
key = 0x20
cipher = bytes([x ^ key for x in raw])
hx = cipher.hex()

print()
print("=== TASK1 ===")

print("text         :", text)
print("raw          :", raw)
print("type(text)   :", type(text))
print("type(raw)    :", type(raw))

print()
print("=== TASK2 ===")

print("list(raw)    :", list(raw))
print("first byte   :", raw[0])
print("chr(65)      :", chr(65))
print("raw2         :", bytes([65, 66, 67]))

print()
print("=== TASK3 ===")

print("raw hex      :", raw.hex())

raw2 = bytes.fromhex("414243")

print("raw2         :", raw2)
print("plain text   :", raw2.decode())

print()
print("=== TASK4 ===")

p = ord("A")
k = 0x20
c = p ^ k
r = c ^ k

print("plaintext    :", p)
print("key          :", k)
print("cipher       :", c)
print("cipher text  :", chr(c))
print("recovered    :", r)
print("plain text   :", chr(r))

print()
print("=== TASK5 ===")

print("raw          :", raw)
print("cipher       :", cipher)
print("cipher hex   :", hx)

recovered = bytes([x ^ key for x in cipher])

print("recovered    :", recovered)
print("plain text   :", recovered.decode())

print()
print("=== TASK6 ===")

print(1 ^ 1)
print(1 ^ 0)
print(0 ^ 1)
print(0 ^ 0)

print()
print(bin(0x41))
print(bin(0x20))
print(bin(0x41 ^ 0x20))

print()
print(65)
print(hex(65))
print(bin(65))
