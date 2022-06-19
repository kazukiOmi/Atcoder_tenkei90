H, W = list(map(int, input().split()))
if H == 1 or W == 1:
    print(H*W)
else:
    ans = (W+1)//2
    ans = ans * ((H+1)//2)
    print(ans)
