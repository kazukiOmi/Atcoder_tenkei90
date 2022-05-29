import sys

n = int(input())
home_list = list(map(int, input().split()))
school_list = list(map(int, input().split()))
home_list.sort()
school_list.sort()

ans = 0
for i in range(n):
    ans += int(abs(home_list[i] - school_list[i]))
print(ans)
