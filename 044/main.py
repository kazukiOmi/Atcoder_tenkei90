import sys


n, q = list(map(int, input().split()))
A = list(map(int, input().split()))

shift = 0
for i in range(q):
    t, x, y = list(map(int, input().split()))
    x, y = x-1, y-1

    x1 = (x-shift) % n
    y1 = (y-shift) % n

    if t == 1:
        A[x1], A[y1] = A[y1], A[x1]
    elif t == 2:
        shift += 1
    else:
        print(A[x1])
