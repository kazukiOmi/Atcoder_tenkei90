N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for a, b in zip(A, B):
    diff += abs(a-b)
if K-diff < 0:
    print("No")
elif (K-diff) % 2 == 0:
    print("Yes")
else:
    print("No")
