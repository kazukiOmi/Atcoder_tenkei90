large_list = []
set = set()


def solve1(N, M, ab_list):
    for a, b in ab_list:
        if a < b:
            small, large = a, b
        else:
            small, large = b, a
        if large not in large_list:
            large_list.append(large)
        else:
            set.add(large)
    print(N-len(set)-(N-len(large_list)))


def solve2(N, M, ab_list):
    edge = [0]*N
    for a, b in ab_list:
        if a < b:
            edge[b-1] += 1
        else:
            edge[a-1] += 1
    print(edge.count(1))


N, M = list(map(int, input().split()))
ab_list = [list(map(int, input().split())) for _ in range(M)]
# solve1(N, M, ab_list)
solve2(N, M, ab_list)
