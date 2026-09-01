a = 5  # 0000 0101
b = 3  # 0000 0011
print(a & b)  # 0000 0001
print(a | b)  # 0000 0111
print(a ^ b)  # 0000 0110
print(a << b)
print(40 >> b)
print(~a)

# 멤버쉽 연산자
print("a" in "apple")
print(3 in [1, 2, 3])



#삼향 연산자.
#int max = a>b?a:b;
#↓
max_num = a if a>b else b

#a 값이 짝수면 "짝수" 아니면 "홀수"
result = "짝수" if a % 2 == 0 else "홀수"
print(result)

score = 100
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" 
print(result)
