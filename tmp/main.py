import sys


n = int(input())
rate_list = list(map(int, input().split()))
# rate_list = [869120000, 998244353, 777777777, 123456789, 100100100,
#              464646464, 987654321, 252525252, 869120001, 1000000000]
rate_list.sort()
num_stu = int(input())

for i in range(num_stu):
    left = 0
    right = n-1
    mid = n//2
    rate = int(input())
    if rate_list[left] == rate or rate_list[right] == rate:
        print(0)
        continue
    while(right-left) > 1:
        if rate < rate_list[mid]:
            right = mid
        elif rate > rate_list[mid]:
            left = mid
        else:
            right = mid
            break
        mid = (left+right)//2
    print(min(abs(rate_list[left]-rate), abs(rate_list[right]-rate)))
