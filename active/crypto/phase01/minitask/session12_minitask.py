print()
print("=== MINI TASK ===")
print()

token = b"65794a68624763694f694a49557a49314e694a392e65794a7a645749694f694a6f6232316c496e302e736967"
hex_chars = "1234567890abcdefABCDEF"
token_is_hex = all(c in hex_chars for c in token.decode())
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_="
token_is_base64 = all(c in base64_chars for c in token.decode())
token_is_jwt_like = "." in token.decode()
token_text = token.decode()
segments = token_text.split(".")
segments_count = len(segments)

print(f"{token = }")
print(f"{type(token) = }")
print(f"{token.decode().isprintable() = }")
print(f"{token_is_hex = }")
print(f"{token_is_base64 = }")
print(f"{token_is_jwt_like = }")
print(f"{segments_count = }")
print()
print("=== peel ONE layer ===")
print()

peel = bytes.fromhex(token_text)
peel_text = peel.decode()
peel_is_jwt_like = "." in peel_text
peel_segments = peel_text.split(".")
peel_segments_is_jwt = len(peel_segments) == 3

print(f"{peel = }")
print(f"{type(peel) = }")
print(f"{peel_is_jwt_like = }")
print(f"{peel_segments = }")
print(f"{peel_segments_is_jwt = }")
