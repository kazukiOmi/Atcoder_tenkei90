N = int(input())
S = input()

l = []

past = ""
count = 0
for s in S:
    if s != past:
        l.append(1)
        past = s
    else:
        l[-1] += 1
k = N
ans = 0
for v in l:
    ans += v*(k-v)
    k -= v
print(ans)
