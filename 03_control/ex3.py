#for 문

#for(int i=0;i<a;i++)

#for i in iterable 객체:

#0~4

for i in range(5):
    print(i,end=" ")
print()


a=range(5)

#print(a.start, a.stop, a,step)

for i in range(1,6):
    print(i,end=" ")
print()

for i in range(5,0,-1):
    print(i,end=" ")
print()

# 1~10 까지 합
tot = 0;
for i in range(1,11):
    tot+=i
else:
    print(f"sum={tot}");

print(sum(range(1,11)))
s="aaa황유찬@#!"

for c in s:
    print(c,end=" ")
print()
print(len(s))

#구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}*{j}={i*j:<5d}",end=" ")
    print()