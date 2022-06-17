H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(H-1):
    for j in range(W-1):
        if A[i][j] != B[i][j]:
            t = B[i][j] - A[i][j]
            A[i][j] += t
            A[i][j+1] += t
            A[i+1][j] += t
            A[i+1][j+1] += t
            ans += abs(t)
A_h = A[-1]
A_w = [a[-1] for a in A]
B_h = B[-1]
B_w = [b[-1] for b in B]

if A_h == B_h and A_w == B_w:
    print("Yes")
    print(ans)
else:
    print("No")
