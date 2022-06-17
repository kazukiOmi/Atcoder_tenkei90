n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
ans = 1
for a in A:
    ans *= sum(a)

print(ans % (10**9+7))
