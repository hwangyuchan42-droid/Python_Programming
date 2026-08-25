# 파이썬 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형 - 정수형 (int)

a = 10
print(a, type(a))
# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
print(ord("a"))
print(chr(65))

# int 자료형의 크기

x = 10**100
print(x)

# 오버플로우 테스트

a = 2**31 - 1
print(a)
a = a + 1
print(a)

# 실수형(float)
b = 3.14
print(b, type(b))

# float 자료형의 크기
# 부동 소수점 방식
# 64비트 부호, 11비트 지수, 52비트 가수
import sys

print(sys.float_info.min)
print(sys.float_info.max)

print(-sys.float_info.min)
print(-sys.float_info.max)

a = 1.7e308
b = 1.8e308
print(a, b)

# 실수의 오차
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

# 형변환
print(float(10))
print(int(3.14))
print(float("3.14"))
print(int("10"))
