N = int(input())
for i in range(2**N):
    num = 0
    ans = ""
    for j in range(N):
        t = i
        t = i >> (N-1-j)
        if t % 2 == 0:
            num += 1
            ans += "("
        else:
            num -= 1
            ans += ")"
        if num < 0:
            break
    if num == 0:
        print(ans)
