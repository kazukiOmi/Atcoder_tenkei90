import sys


n, k = list(map(int, input().split()))

ab_list = [list(map(int, input().split())) for _ in range(n)]

a_list = [b for _, b in ab_list]
b_list = [a-b for a, b in ab_list]
a_list.extend(b_list)
new_a_list = sorted(a_list, reverse=True)
ans = 0
for v in new_a_list[:k]:
    ans += v
print(ans)
