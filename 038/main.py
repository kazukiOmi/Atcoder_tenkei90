import sys
import math


a, b = list(map(int, input().split()))
lcm = a*b//math.gcd(a, b)
if lcm > 10**18:
    print("Large")
else:
    print(lcm)
