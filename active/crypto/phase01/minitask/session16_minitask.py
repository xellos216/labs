import base64
import json


def is_json_like(data: bytes):
    try:
        text = data.decode()
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
        return None

    except Exception:
        return None


def is_timestamp_like(value) -> bool:
    if not isinstance(value, int):
        return False

    if 1_000_000_000 <= value <= 9_999_999_999:
        return True

    if 1_000_000_000_000 <= value <= 9_999_999_999_999:
        return True

    return False


def find_timestamp_like_fields(obj: dict):
    results = []

    for key, value in obj.items():
        if key in ("exp", "iat", "nbf") and is_timestamp_like(value):
            results.append((key, value))

    return results


def print_modification_verification_reasoning(segment_role: str):
    if segment_role == "payload-like":
        print("readable = True")
        print("modifiable_attempt = True")
        print("valid_modification_without_key = False")
        print(
            "reason = payload can be edited, but modified payload needs a valid signature"
        )
    elif segment_role == "metadata/header-like":
        print("readable = True")
        print("modifiable_attempt = True")
        print("valid_modification_without_key = False")
        print(
            "reason = header can be edited, but signature verification should fail if protected input changes"
        )
    elif segment_role == "signature/integrity-like":
        print("readable = False or low-semantic-readability")
        print("modifiable_attempt = True")
        print("valid_modification_without_key = False")
        print(
            "reason = signature is verification data; random modification should break integrity"
        )
    else:
        print("readable = unknown")
        print("modifiable_attempt = True")
        print("valid_modification_without_key = unknown")


def print_integrity_auth_reasoning(has_signature_like: bool):
    if has_signature_like:
        print("integrity_reasoning = signature-like segment exists")
        print(
            "authentication_reasoning = valid signature would imply issuer/key-holder authenticity"
        )
        print("verified = False")
        print(
            "reason = structure suggests integrity/authentication, but no secret/public key verification was performed"
        )
    else:
        print("integrity_reasoning = no signature-like segment observed")
        print("authentication_reasoning = weak or unknown")
        print("verified = False")


print("=== MINI TASK ===")
print()

token = b"ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKeWIyeGxJam9pWjNWbGMzUWlmUS5jMmxuYm1GMGRYSmw="
hex_str = "0123456789abcdefABCDEF"
base64_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ=_"
is_hex_like = all(c in hex_str for c in token.decode())
is_base64_like = all(c in base64_str for c in token.decode())
base64_decode = base64.urlsafe_b64decode(token)
parts = base64_decode.decode().split(".")

print(f"{token = }")
print(f"{token.decode() = }")
print()
print(f"{is_hex_like = }")
print(f"{is_base64_like = }")
print()
print(f"{base64_decode = }")
print(f"{parts = }")
print(f"{len(parts) = }")
print()
has_signature_like = False

for i, part in enumerate(parts):
    padded = part + "=" * (-len(part) % 4)

    try:
        decoded = base64.urlsafe_b64decode(padded)
        text = decoded.decode(errors="replace")
        parsed = is_json_like(decoded)

        print("segment", i)
        print(f"{decoded = }")

        if parsed is not None:
            print("json_like = True")
            print(f"{parsed = }")

            timestamp_fields = find_timestamp_like_fields(parsed)
            print(f"{timestamp_fields = }")
        else:
            print("json_like = False")
            print("timestamp_fields = []")

        if "alg" in text:
            semantic_guess = "metadata/header-like"
        elif "user" in text or "admin" in text or "role" in text:
            semantic_guess = "payload-like"
        else:
            semantic_guess = "signature/integrity-like or unknown"

        if semantic_guess.startswith("signature"):
            has_signature_like = True

        print(f"{semantic_guess = }")
        print_modification_verification_reasoning(
            "signature/integrity-like"
            if semantic_guess.startswith("signature")
            else semantic_guess
        )

    except Exception:
        print("segment", i)
        print("not valid base64")
        print(part)

    print()

print_integrity_auth_reasoning(has_signature_like)
