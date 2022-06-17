N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
lrv = [list(map(int, input().split())) for _ in range(Q)]

diff_list = []
diff_sum = 0
for i in range(N-1):
    tmp = A[i+1]-A[i]
    diff_list.append(tmp)
    diff_sum += abs(tmp)


for l, r, v in lrv:
    if l > 1:
        diff_sum -= abs(diff_list[l-2])
        diff_list[l-2] += v
        diff_sum += abs(diff_list[l-2])
    if r < N:
        diff_sum -= abs(diff_list[r-1])
        diff_list[r-1] -= v
        diff_sum += abs(diff_list[r-1])
    print(diff_sum)
