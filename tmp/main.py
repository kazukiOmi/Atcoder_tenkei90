import sys

input = sys.stdin.readline

n, q = list(map(int, input().split()))
sequence = list(map(int, input().split()))

shift = 0
for i in range(q):
    t, x, y = list(map(int, input().split()))
    x, y = x-1, y-1

    x1 = (x-shift) % n
    y1 = (y-shift) % n

    if t == 1:
        sequence[x1], sequence[y1] = sequence[y1], sequence[x1]
    elif t == 2:
        shift += 1
        # shift %= n
    else:
        print(sequence[x1])
