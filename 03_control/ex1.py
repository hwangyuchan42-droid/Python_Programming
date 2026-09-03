#조건문 

age = 17
if age >= 18:
    print("청년")
else:
    print("미성년")

score = 100
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


#match 문

grade = "A"
match grade:
    case "A":
        print("우수")
    case "B":
        print("양호")
    case "C":
        print("보통")
    case _:
        print("알 수 없음")
