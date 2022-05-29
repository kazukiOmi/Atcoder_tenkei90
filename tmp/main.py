import sys


def func(v, n):
    if (int(v / n)):
        return func((v // n), n) + str(v % n)
    return str(v % n)


input = sys.stdin.readline

n, k = input().split()
# print(n)
k = int(k)

for i in range(k):
    ten_base = int(n, 8)
    # print(ten_base)
    nine_base = func(ten_base, 9)
    # print(nine_base)
    nine_base = nine_base.replace("8", "5")
    n = nine_base
print(nine_base)
