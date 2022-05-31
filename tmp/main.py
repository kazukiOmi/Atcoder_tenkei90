import sys
from itertools import permutations


input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())


uwasa = {}
for _ in range(m):
    x, y = list(map(int, input().split()))
    x, y = x-1, y-1
    if x not in uwasa:
        uwasa[x] = [y]
    else:
        uwasa[x].append(y)
    if y not in uwasa:
        uwasa[y] = [x]
    else:
        uwasa[y].append(x)
# print(uwasa)


ans = 10001

for i in permutations(range(n)):
    # print(i)
    can_goal = True
    for j in range(n-1):
        if i[j] in uwasa:
            if i[j+1] in uwasa[i[j]]:
                can_goal = False
                break
    if can_goal:
        # print(i)
        tmp = 0
        order = 0
        for k in i:
            tmp += a[k][order]
            order += 1
        if tmp < ans:
            ans = tmp
if ans < 10001:
    print(ans)
else:
    print(-1)
