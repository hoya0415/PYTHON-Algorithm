import sys
sys.stdin = open('./1459_input.txt')

X, Y, W, S = map(int, input().split())
res = 0
if W > S:
    if abs(X-Y) % 2:
        print((min(X, Y) * S) + ((max(X, Y) - min(X, Y) - 1) * S) + W)
    else:
        print((min(X, Y) * S) + ((max(X, Y)-min(X, Y)) * S))

elif W * 2 > S:
    print((min(X, Y) * S) + ((max(X, Y)-min(X, Y)) * W))
else:
    print((X+Y) * W)