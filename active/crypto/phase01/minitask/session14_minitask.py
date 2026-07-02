import base64
import json

print("=== MINI TASK ===")
print()


def is_json_like(data: bytes) -> bool:
    try:
        text = data.decode()
        parsed = json.loads(text)
        return isinstance(parsed, (dict, list))
    except Exception:
        return False


token = b"ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWVdSdGFXNGlmUS5jMmxuYm1GMGRYSmw="
token_decode = token.decode()

hex_str = "0123456789abcdefABCDEF"
base64_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_="

token_decode_is_hex = len(token_decode) % 2 == 0 and all(
    c in hex_str for c in token_decode
)

token_decode_is_base64 = all(c in base64_str for c in token_decode)
token_segment_count = len(token_decode.split("."))

peel_layer = base64.b64decode(token)
peel_layer_decode = peel_layer.decode()
peel_segment_count = len(peel_layer_decode.split("."))

parts = peel_layer_decode.split(".")

print(f"{token = }")
print(f"{token_decode = }")
print()
print(f"{type(token) = }")
print(f"{type(token_decode) = }")
print()
print(f"{token_decode_is_hex = }")
print(f"{token_decode_is_base64 = }")
print(f"{token_segment_count = }")
print()
print(f"{peel_layer = }")
print(f"{peel_layer_decode = }")
print(f"{peel_segment_count = }")
print()
for i, part in enumerate(parts):
    padded = part + "=" * (-len(part) % 4)

    try:
        decoded = base64.urlsafe_b64decode(padded)
        print("segment", i)
        print(f"{decoded = }")

        if is_json_like(decoded):
            print("json_like = True")
        else:
            print("json_like = False")

    except Exception:
        print("segment", i)
        print("not valid base64")
        print(part)
    print()

print("There is no timestamp-like field")
