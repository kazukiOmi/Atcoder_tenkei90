N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]

node_connect = {}
node_connect[1] = []
for a, b in AB:
    if a not in node_connect:
        node_connect[a] = [b]
    else:
        node_connect[a].append(b)
    if b not in node_connect:
        node_connect[b] = [a]
    else:
        node_connect[b].append(a)

ans = [None, 0]
stock_list = [1]
depth_from_1 = {1: 0}
while(len(depth_from_1) != N):
    visit_node = stock_list.pop(0)
    for node in node_connect[visit_node]:
        if node not in depth_from_1:
            stock_list.append(node)
            depth_from_1[node] = depth_from_1[visit_node]+1
            if ans[1] < depth_from_1[node]:
                ans = [node, depth_from_1[node]]


ans2 = 0
stock_list = [ans[0]]
node_dict3 = {ans[0]: 0}
while(len(node_dict3) != N):
    visit_node = stock_list.pop(0)
    for node in node_connect[visit_node]:
        if node not in node_dict3:
            stock_list.append(node)
            node_dict3[node] = node_dict3[visit_node]+1
            if ans2 < node_dict3[node]:
                ans2 = node_dict3[node]
print(ans2+1)
