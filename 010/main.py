import sys

n = int(input())

one_list = []
two_list = []

sum_one = 0
sum_two = 0
one_list.append(0)
two_list.append(0)
for _ in range(n):
    cls, score = list(map(int, input().split()))
    if cls == 1:
        sum_one += score
    else:
        sum_two += score
    one_list.append(sum_one)
    two_list.append(sum_two)

q = int(input())

for _ in range(q):
    start, end = list(map(int, input().split()))
    print(
        f"{one_list[end]-one_list[start-1]} {two_list[end]-two_list[start-1]}")
