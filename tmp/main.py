import sys
import math

# input = sys.stdin.readline


# def combinations_count(n, r):
# return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def combinations_count(n, r):
    ans = 1
    bunbo = 1
    s = 1
    for i in range(n, n-r, -1):
        ans *= i
        bunbo *= s
        s += 1
    return ans // bunbo


n, l = list(map(int, input().split()))
ans = 0
use_max_l = n // l

for i in range(use_max_l+1):
    total = n-(l*i)+i
    ans += combinations_count(total, i)
# print(ans)
print(ans % (10**9+7))
