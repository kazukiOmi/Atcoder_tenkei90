L, R = list(map(int, input().split()))

ans = 0

l_keta = len(str(L))
r_keta = len(str(R))


ans = 0
if l_keta == r_keta:
    kousuu = R-L+1
    ans += (((kousuu)*(2*L+kousuu-1))*l_keta)//2 % (10**9+7)
    print(ans % (10**9+7))
else:
    l_kousuu = 10**l_keta-L
    ans += ((((l_kousuu)*(2*L+l_kousuu-1))*l_keta)//2) % (10**9+7)
    r_kousuu = R-10**(r_keta-1)+1
    ans += (((r_kousuu)*(2*(10**(r_keta-1))+r_kousuu-1))*r_keta)//2 % (10**9+7)
    for i in range(l_keta+1, r_keta, 1):
        kousuu = 10**i-10**(i-1)
        ans += (((kousuu)*(2*10**(i-1)+kousuu-1))*i)//2 % (10**9+7)
    print(ans % (10**9+7))
