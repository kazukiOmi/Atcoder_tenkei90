N, P, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [a % P for a in A]

ans = 0
for i in range(N-4):
    for j in range(i+1, N-3):
        t0 = (A[i]*A[j]) % P
        for k in range(j+1, N-2):
            t1 = (t0*A[k]) % P
            for l in range(k+1, N-1):
                t2 = (t1*A[l]) % P
                for m in range(l+1, N):
                    if (t2*A[m]) % P == Q:
                        ans += 1
print(ans)
