#!/usr/bin/env python3

import base64

print("=== STEP1 ===")

A = b"6865c6c6f"
B = b"aGVsbG8="
C = b"4f2a1b9c"
D = b"U0dWc2JHOD0"
E = b"7b2261646d696e223a747275657d"

print(f"{A = }")
print(f"{B = }")
print(f"{C = }")
print(f"{D = }")
print(f"{E = }")

print()

print(type(A))
print(type(B))
print(type(C))
print(type(D))
print(type(E))

print()
print("=== STEP2 ===")

print("token")
print("-> aGVsbG8=")

print()
print("=== STEP3 ===")

print("plaintext")
print("-> hex")
print("-> base64")
print("-> token")

print()
print("=== STEP4 ===")
A = b"hello"
B = "68656c6c6f"
C = b"68656c6c6f"
D = b"aGVsbG8="
E = base64.b64decode(b"aGVsbG8=")

print()

print(f"{A = }")
print(f"{B = }")
print(f"{C = }")
print(f"{D = }")
print(f"{E = }")

print("A = raw bytes")
print("B = plaintext str")
print("C = hex wrapper")
print("D = base64 wrapper")
print("E = printable wrapper bytes")

print()
print("=== STEP5 ===")

token = b"4d5467794d7a5131"
token_decode = token.decode()


print(f"{token =}")
print(f"{token_decode = }")


print()
print("=== Mini Task ===")

token_b64d = base64.b64decode(token)
token_hex = token.hex()

print(f"{token = }")
print(f"token type is {type(token)}")
print()
print(f"{token_decode = }")
print(f"token_decode type is {type(token_decode)}")
print()
print(f"{token_b64d = }")
print(f"token_b64d type is {type(token_b64d)}")
print()
print(f"{token_hex = }")
print(f"token_hex type is {type(token_hex)}")
