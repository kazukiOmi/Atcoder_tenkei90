from email.mime import base
import sys


def base46(x):
    return int(x) % 46


input = sys.stdin.readline
# a = list(map(base46, input().split()))
# b = list(map(base46, input().split()))
# c = list(map(base46, input().split()))

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_dict = {}
b_dict = {}
c_dict = {}
for i in range(46):
    a_dict[i] = 0
    b_dict[i] = 0
    c_dict[i] = 0


for ai, bi, ci in zip(a, b, c):
    at, bt, ct = ai % 46, bi % 46, ci % 46
    a_dict[at] += 1
    b_dict[bt] += 1
    c_dict[ct] += 1
ans = 0
for i in range(46):
    for j in range(46):
        base_46 = (46-(i+j)) % 46
        ans += a_dict[i]*b_dict[j]*c_dict[base_46]
print(ans)
