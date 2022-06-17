import math


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())
arr = factorization(N)
ruizyou_list = [a[1] for a in arr]
sum_ruizyou = sum(ruizyou_list)
ans = math.log2(sum_ruizyou)
if ans.is_integer():
    print(int(ans))
else:
    print(int(ans+1))
