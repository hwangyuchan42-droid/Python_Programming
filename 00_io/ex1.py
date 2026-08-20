# aa
#include
#입출력
a = input()
print(a,end="")
print(type(a));
print(a, type(a), sep=", ");

#정수 변환
a= input();
a=int(a)
print(a, type(a), sep=", ");


a=int(input())
print(a, type(a))
b=float(input())
print(b,type(b))


a= int(input())
b= int(input())

print(a,b);

a=input().split()
print(a, type(a))



#map

a,b,c =map(int, input().split())
print(a, type(a))
a = list(map(int, input().split()))
print(a, type(a))