print("=== MINI TASK ===")
print()

token = b"65794a68624763694f694a49557a49314e694a392e65794a3163325679496a6f695a33566c6333516966512e63326c6e"
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_="
hex_chars = "0123456789abcdefABCDEF"

token_decode = token.decode()
token_decode_is_hex = len(token_decode) % 2 == 0 and all(
    c in hex_chars for c in token_decode
)

peeled = bytes.fromhex(token_decode)
peeled_text = peeled.decode()

is_jwt_like = "." in peeled_text and len(peeled_text.split(".")) == 3

segments = peeled_text.split(".")
segments_are_base64_like = all(
    all(c in base64_chars for c in segment) for segment in segments
)

print(f"{token = }")
print(f"{type(token) = }")
print()
print(f"{token_decode = }")
print(f"{type(token_decode) = }")
print(f"{token_decode_is_hex = }")
print(f"{token_decode.isprintable() = }")
print()
print(f"{peeled = }")
print(f"{peeled_text= }")
print(f"{type(peeled) = }")
print(f"{type(peeled_text) = }")
print()
print(f"{segments = }")
print(f"{is_jwt_like = }")
print(f"{segments_are_base64_like = }")
