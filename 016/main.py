import sys
from numba import njit


n = int(input())
kouka_list = list(map(int, input().split()))
kouka_list.sort(reverse=True)
a, b, c = kouka_list


@njit(cache=True)
def ans(n, a, b, c):
    ans = 9999
    max_num_c = min(n // c, 9999)
    for i in range(max_num_c+1):
        c_money = c * i
        max_num_b = min((n - c_money) // b, 9999)
        for j in range(max_num_b+1):
            cb_money = c_money+b*j
            if (n-cb_money) % a == 0:
                k = (n-cb_money) // a
                ans = min(ans, i+j+k)
    print(ans)


ans(n, a, b, c)
