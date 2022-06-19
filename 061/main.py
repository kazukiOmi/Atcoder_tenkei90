Q = int(input())
tx = [list(map(int, input().split())) for _ in range(Q)]

deck = []

for t, x in tx:
    if t == 1:
        deck.insert(0, x)
    elif t == 2:
        deck.append(x)
    else:
        print(deck[x-1])
