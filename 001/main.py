N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split())) + [L]
diff = []
tmp = 0
for a in A:
    diff.append(a-tmp)
    tmp = a
left = 1
right = L//(K+1)
while(left < right):
    mean = (left+right+1)//2
    size = 0
    pieces = 0
    for v in diff:
        size += v
        if size >= mean:
            pieces += 1
            size = 0
    if pieces > K:
        left = mean
    else:
        right = mean-1
print(left)
