import base64
import sys
from pathlib import Path


def read_token():
    if len(sys.argv) >= 2:
        value = sys.argv[1]
    else:
        value = input("token or filename: ").strip()

    if Path(value).exists():
        return Path(value).read_text().strip()

    return value


def decode_segment(part):
    padded = part + "=" * (-len(part) % 4)
    decoded = base64.urlsafe_b64decode(padded)
    text = decoded.decode(errors="replace")

    return decoded, text


def guess_role(text):
    if "alg" in text or "typ" in text:
        return "metadata/header-like"
    elif "user" in text or "role" in text or "exp" in text:
        return "payload-like /claims-like"
    else:
        return "integrity/signature-like or unknown"


def analyze_token(token):
    parts = token.split(".")
    roles = []
    decoded_segments = []

    for part in parts:
        decoded, text = decode_segment(part)
        decoded_segments.append(text)
        roles.append(guess_role(text))

    capabilities = []

    if any("alg" in text or "typ" in text for text in decoded_segments):
        capabilities.append("inspect metadata")

    if any("user" in text or "role" in text for text in decoded_segments):
        capabilities.append("inspect claims")
        capabilities.append("read user role")

    return parts, roles, decoded_segments, capabilities


def print_report(token, parts, roles, decoded_segments, capabilities):
    print()
    print("=== ANALYSIS REPORT ===")
    print()

    print("representation:")
    print(f"type = {type(token)}")
    print(f"printable = {token.isprintable()}")

    print()
    print("structure:")
    print(f"segment_count = {len(parts)}")
    print(f"jwt_like = {'.' in token}")
    print(f"jwt_len_like = {len(parts) == 3}")

    print()
    print("semantic roles:")
    for i, role in enumerate(roles):
        print(f"segment {i} -> {role}")

    print()
    print("capabilities:")
    for capability in capabilities:
        print(f"- {capability}")

    print()
    print("""verification state:
    unknown / not verified""")

    print()
    print("""security reasoning:
    payload is readable, but readable does not imply trusted
    signature verification has not been performed
    claims should not be trusted yet""")


def main():
    token = read_token()
    parts, roles, decoded_segments, capabilities = analyze_token(token)
    print_report(token, parts, roles, decoded_segments, capabilities)


if __name__ == "__main__":
    main()

print()
