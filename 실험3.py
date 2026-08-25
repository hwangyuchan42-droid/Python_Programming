#n개의 숫자를 입력받았을 떄 원소들을 제ㅔ배열하여 차의 총합이 가장 클 때의 값을 구하는 프로그램을 작성하시오.
n = int(input())
a = list(map(int, input().split()))
a.sort()
max_sum = 0
for i in range(n//2):
    max_sum += a[n-i-1] - a[i]
print(max_sum)
