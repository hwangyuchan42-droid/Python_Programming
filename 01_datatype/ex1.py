#변수
a = 2
b = 3
print(a, b)
#int a=2,b=3 ==> int a=(2,b)=3
a=2;b=3;

a,b = 2,3 # 권장 #앞의 쉼표는 튜플 언패킹이고, 뒤는 튜플 안의 값이 맞음;
print(a, b)
# 값 swap
temp = a
a = b
b = temp

print(a, b)

a,b = b,a;
print(a, b)


x = y = z = 0

print(x, y, z)

#변수명 규칙(C와 동일)

# 1. 변수명은 알파벳, 숫자, 밑줄(_)만 사용할 수 있다.
# 2. 변수명은 숫자로 시작할 수 없다.
# 3. 변수명은 대소문자를 구분한다.
# 4. 변수명은 예약어를 사용할 수 없다.
# 5. 변수명은 의미 있는 이름을 사용하는 것이 좋다.

name1 = "뽀로로"

print(name1)

이름 = "에디" #비권장 

student_name = "루피" #snake_case #권장
studentName = "포비" #camelCase

#상수(없음)
MAX_SCORE = 100 #상수처럼 사용
