import sys
import math


n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(q)]

diff_list = []
for i in range(n-1):
    diff_list.append(a[i+1]-a[i])

tmp = [abs(x) for x in diff_list]
ans = sum(tmp)
for left, right, v in l:
    if left > 1:
        ans -= abs(diff_list[left-2])
        diff_list[left-2] += v
        ans += abs(diff_list[left-2])
    if right < n:
        ans -= abs(diff_list[right-1])
        diff_list[right-1] -= v
        ans += abs(diff_list[right-1])
    # print(diff_list)
    print(ans)
