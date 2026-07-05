import base64

print("=== MINI TASK ===")
print()

token = "helloworld"

print(f"{token = }")
print(f"{type(token) = }")
print(f"{token.isprintable() = }")
print()

print("=== hex like? ===")
print()

hex_chars = "0123456789abcdefABCDEF"
is_hex = all(c in hex_chars for c in token)
print(f"{hex_chars = }")
print(f"{is_hex = }")
print()

print("=== base64 like ===")
print()

decoded = None

try:
    decoded = base64.b64decode(token)
    print(decoded)
except:
    print("not base64")

print(f"{decoded = }")
