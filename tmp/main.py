import sys
import math
import functools

input = sys.stdin.readline

no_list = list(map(int, input().split()))
gcd = functools.reduce(math.gcd, no_list)
# print(gcd)
print((no_list[0]//gcd)+(no_list[1]//gcd)+(no_list[2]//gcd)-3)
