#N개의 정수로 이루어진 배열 A가 무작위로 주어졌을 때, 배열 A의 원소를 재배열하여 원소 사이간의 차의 총합이 가장 클 때의 값을 구하는 프로그램을 작성하시오.예로는 3\n1,2,3은 3, 5/n 1,2,3,4,5 는 11이 나오게.
n = int(input())
a = list(map(int, input().split()))
a.sort()
max_sum = 0
for i in range(n//2):
    max_sum += a[n-i-1] - a[i]
print(max_sum)
