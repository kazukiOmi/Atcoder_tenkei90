import sys

input = sys.stdin.readline

a, b, c = list(map(int, input().split()))
if a < c**b:
    print("Yes")
else:
    print("No")
