#반복문 : while문, for 문

#while문
#1~10 까지 반복 출력
# i=1;
# while i<=10:
#     print(i)
#     i+=1
#     if(i==5):
#         break;
# else:
#     print("End");

# nums = [1,3,5,7,9]
# target = 2

# while nums:
#     print("found")
# else:
#     print("not found")

# while i<len(nums):
#     if(nums[i])==target:
#         print(f"{target}  found.")
#         break
#     i+=1
# else:
#     print(f"{target} not found.")

i=1
tot = 0
while(i<=10):
    if i%2 ==0:
        tot+=i
        
    i+=1;
else:
    print(f"합:{tot}")

