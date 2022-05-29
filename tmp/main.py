import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
diff_list = [abs(a_list[i]-b_list[i]) for i in range(n)]
# print(diff_list)
diff_sum = sum(diff_list)
amari = k-diff_sum
if amari < 0:
    print("No")
elif amari == 0:
    print("Yes")
else:
    if amari % 2 == 0:
        print("Yes")
    else:
        print("No")
