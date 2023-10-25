
# create_header

room_name = "ゲーム"
operation = 1
header = bytes([len(room_name), operation, 0]) + b"0" * 29


# サーバーに部屋名が正確に入力されない問題修正
body = b'\xe9\x83\xa8\xe5\xb1\x8b\xef\xbc\x91\xe3\x83\xa6\xe3\x83\xbc\xe3\x82\xb6\xe3\x83\xbc\xef\xbc\x91'
decoded_body = body.decode("utf-8")


# 数字を定義
number = 123456

# 数字をバイト化
# ここでは、4バイトのbig-endian表現を想定しています。
byte_data = number.to_bytes(1, 'big')

# バイト数を確認
byte_count = len(byte_data)

print(f"Original Number: {number}")
print(f"Encoded Data: {byte_data}")
print(f"Byte Count: {byte_count}")