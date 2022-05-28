import sys

n = int(input())

one_list = []
two_list = []

sum_one = 0
sum_two = 0
one_list.append(0)
two_list.append(0)
for i in range(n):
    cls, score = list(map(int, input().split()))
    if cls == 1:
        sum_one += score
    else:
        sum_two += score
    one_list.append(sum_one)
    two_list.append(sum_two)

q = int(input())

for i in range(q):
    start, end = list(map(int, input().split()))
    print(
        f"{one_list[end]-one_list[start-1]} {two_list[end]-two_list[start-1]}")


# one_list = []
# total_list = []
# for i in range(n):
#     cls, score = list(map(int, input().split()))
#     if cls == 1:
#         one_list.append(score)
#     else:
#         one_list.append(0)
#     total_list.append(score)
# q = int(input())

# for i in range(q):
#     start, end = list(map(int, input().split()))
#     sum_one = sum(one_list[start-1:end])
#     sum_total = sum(total_list[start-1:end])
#     print(f"{sum_one} {sum_total-sum_one}")
