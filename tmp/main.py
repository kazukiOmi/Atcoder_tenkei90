import sys
# import numpy as np
import math

input = sys.stdin.readline

a, b = list(map(int, input().split()))
# lcm = np.lcm(a, b)
lcm = a*b//math.gcd(a, b)
if lcm > 10**18:
    print("Large")
else:
    print(lcm)
