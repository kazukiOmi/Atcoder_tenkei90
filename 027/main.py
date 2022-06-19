import sys

input = sys.stdin.readline
N = int(input())
S = [input() for _ in range(N)]

user_dic = {}
for i, s in enumerate(S):
    if s not in user_dic:
        user_dic[s] = 1
        print(i+1)
