import sys


def binary_search(numbers, value):
    """2分探索，みつかったらそのインデックス，見つからなかったら入るべきインデックス"""
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    if numbers[mid] < value:
        return mid+1
    else:
        return mid


n = int(input())
rate_list = list(map(int, input().split()))
rate_list.sort()
num_stu = int(input())

for _ in range(num_stu):
    rate = int(input())
    mid = binary_search(rate_list, rate)
    if mid == 0:
        print(abs(rate-rate_list[0]))
    elif mid >= n:
        print(abs(rate_list[-1]-rate))
    else:
        print(min(abs(rate_list[mid]-rate), abs(rate_list[mid-1]-rate)))
