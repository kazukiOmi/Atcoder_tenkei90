import sys
import math
import functools


no_list = list(map(int, input().split()))
gcd = functools.reduce(math.gcd, no_list)
print((no_list[0]//gcd)+(no_list[1]//gcd)+(no_list[2]//gcd)-3)
