import base64

print("=== MINI TASK===")
print()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJyb2xlIjoicmVhZGVyIiwiZXhwIjoxNzM1NjgwMDAwfQ.c2lnbmF0dXJlLWJ5dGVz"
parts = token.split(".")

print(f"{token = }")
print(f"{type(token) = }")
print(f"{token.isprintable() = }")
print(f"{'.' in token = }")
print()
print(f"{len(token.split('.')) = }")
print()
print(f"{parts = }")
print()

for i, part in enumerate(parts):
    padded = part + "=" * (-len(part) % 4)
    decoded = base64.urlsafe_b64decode(padded)
    text = decoded.decode(errors="replace")

    print("segment", i)
    print(decoded)
    print(f"{text = }")

    if "alg" in text or "typ" in text:
        print("semantic_role = metadata/header-like")
    elif "user" in text or "role" in text or "exp" in text:
        print("semantic_role = payload-like")
    else:
        print("semantic_role = signature/integrity-like or unknown")

    print()

print("semantic roles:")
print("segment 0 -> metadata/header-like")
print("segment 1 -> payload-like")
print("segment 2 -> integrity/signature-like")

print()
print("capabilities:")
print("readable segments can be inspected")
print("readable does not mean trusted")
print("modification requires valid signature verification")

print()
print("verification state:")
print("unknown")
