import os
secret_value = os.getenv("SECRET_MESSAGE")
secret_value2 = os.getenv("SECRET_MESSAGE2")


if secret_value:
    print("SECRET_MESSAGE 값 읽기 성공")
else:
    print("SECRET_MESSAGE 값이 없음")

if secret_value2:
    print("SECRET_MESSAGE2 값 읽기 성공")
else:
    print("SECRET_MESSAGE2 값이 없음")