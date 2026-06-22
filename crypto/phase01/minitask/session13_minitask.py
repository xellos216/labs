import base64

print("=== MINI TASK ===")
print()

token = b"ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWjNWbGMzUWlmUS5zaWduYXR1cmU="
hex_str = "0123456789abcdefABCDEF"
base64_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890+/="
token_decode = token.decode()
token_is_hex = all(x in hex_str for x in token_decode)
token_is_base64 = all(x in base64_str for x in token_decode)
token_is_segment = len(token_decode.split(".")) == 3

peel_one_layer = base64.b64decode(token)
peel_one_layer_is_segment = len(peel_one_layer.decode().split(".")) == 3

parts = peel_one_layer.decode().split(".")

print(f"{token = }")
print(f"{type(token) = }")
print(f"{token_is_hex = }")
print(f"{token_is_base64 = }")
print(f"{token_is_segment = }")
print()
print(f"{peel_one_layer = }")
print(f"{peel_one_layer_is_segment = }")
print(f"{parts = }")
print()
for i, part in enumerate(parts):
    print(f"{i, part = }")
print()

for i, part in enumerate(parts):
    padded = part + "=" * (-len(part) % 4)

    try:
        decoded = base64.urlsafe_b64decode(padded)

        print("segment", i)
        print(f"{decoded = }")

    except Exception:
        print("segment", i)
        print("not valid base64")
        print(part)

    print()

print("segment0 -> metadata-like\nsegment1 -> payload-like\nsegment2 -> signature-like")
