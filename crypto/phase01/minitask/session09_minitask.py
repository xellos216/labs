token = "minitask"

print(f"{token = }")
print(f"{type(token) = }")
print()

x = token.encode()
print(f"{x =}")
print(f"{type(x) = }")

print()

y = x.hex()
print(f"{y =}")
print(f"{type(y) = }")

print()

z = y.encode()
print(f"{z = }")
print(f"{type(z) = }")

print()

print("=== reverse ===")

a = z.decode()
print(f"{a = }")
print(f"{type(a) = }")

print()

b = bytes.fromhex(a)
print(f"{b = }")
print(f"{type(b) = }")

print()

c = b.decode()
print(f"{c = }")
print(f"{type(c) = }")
