import sys
import math


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 1
for ai in a:
    ans *= sum(ai)

print(ans % (10**9+7))
