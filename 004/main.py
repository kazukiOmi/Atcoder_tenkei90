import sys
import numpy as np

h, w = map(int, input().split())

masu = np.zeros([h, w])

for i in range(h):
    masu[i, :] = np.array(list(map(int, input().split())))

h_sum_list = []
for i in range(h):
    h_sum_list.append(int(np.sum(masu[i, :])))
w_sum_list = []
for i in range(w):
    w_sum_list.append(int(np.sum(masu[:, i])))


for i in range(h):
    tmp_list = []
    for j in range(w):
        tmp = h_sum_list[i] + w_sum_list[j] - int(masu[i, j])
        tmp_list.append(int(tmp))
    print(*tmp_list)
