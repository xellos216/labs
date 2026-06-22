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


token = b"ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKMWMyVnlJam9pWjNWbGMzUWlmUS5jMmxuYm1GMGRYSmw="

token_decode = token.decode()

hex_str = "0123456789abcdefABCDEF"
base64_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz=_"

token_is_hex = all(c in hex_str for c in token_decode)
token_is_base64 = all(c in base64_str for c in token_decode)

peel_one_layer = base64.urlsafe_b64decode(token_decode)

peel_text = peel_one_layer.decode()

parts = peel_text.split(".")

print(f"{token = }")
print(f"{token_is_hex = }")
print(f"{token_is_base64 = }")
print()
print(f"{peel_one_layer = }")
print(f"{peel_text = }")
print()
print(f"{parts = }")
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

    text = decoded.decode(errors="replace")

    if "alg" in text:
        print("semantic_guess = metadata/header-like")
    elif "user" in text or "admin" in text or "role" in text:
        print("semantic_guess = payload-like")
    else:
        print("semantic_guess = signature/integrity-like or unknown")
    print()

print("readable does not mean trusted")
print("segment 0/1 are readable, but modification would require valid signature")
print("segment 2 is likely integrity-related")
print()
