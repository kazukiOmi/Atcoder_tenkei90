import sys
import math


n, k = list(map(int, input().split()))

mod = 10 ** 9 + 7
if n == 1:
    print(k)
else:
    ans = k * (k - 1) * pow(k - 2, n - 2, mod)
    print(ans % mod)

# if n == 1:
#     print(k)
# elif n == 2:
#     print(k*(k-1))
# else:
#     if k < 3:
#         print(0)
#     else:
#         sum = k*(k-1)
#         n2 = k-2
#         r = n-2
#         ans = 1
#         sqrt_r = math.floor(math.sqrt(r))
#         while(True):
#             tmp = (n2**sqrt_r) % (10**9+7)
#             tmp = (tmp**sqrt_r) % (10**9+7)
#             ans = (ans*tmp) % (10**9+7)
#             r = r - sqrt_r**2
#             if r < 4:
#                 break
#             sqrt_r = math.floor(math.sqrt(r))
#         while(r > 0):
#             ans = (ans*(n2)) % (10**9+7)
#             r -= 1
#         sum *= ans
#         print(sum % (10**9+7))
