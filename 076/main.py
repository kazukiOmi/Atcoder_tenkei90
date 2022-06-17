import sys

N = int(input())
A = list(map(int, input().split()))

total = sum(A)
A *= 2


k = total / 10
l, r = 0, 0
tmp = 0
while(l < N):
    while(tmp < k):   # tmp<k(<total)ならr<N+lを満たす
        tmp += A[r]
        r += 1
    if tmp == k:
        print("Yes")
        sys.exit()
    tmp -= A[l]
    l += 1
print("No")
