import sys


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_dict = {}
b_dict = {}
c_dict = {}
for i in range(46):
    a_dict[i] = 0
    b_dict[i] = 0
    c_dict[i] = 0

for a, b, c in zip(A, B, C):
    at, bt, ct = a % 46, b % 46, c % 46
    a_dict[at] += 1
    b_dict[bt] += 1
    c_dict[ct] += 1
ans = 0
for i in range(46):
    for j in range(46):
        k = (46-(i+j)) % 46
        ans += a_dict[i]*b_dict[j]*c_dict[k]
print(ans)
