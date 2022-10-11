import sys
sys.stdin = open('./18512_input.txt')

X, Y, Pa, Pb = map(int, input().split())

A = []
B = []
if abs(X-Y) == 0 and abs(Pa-Pb) < X:
    print(-1)
else:
    flag = 0
    for i in range(1000):
        a = X * i + Pa
        b = Y * i + Pb
        A.append(a)
        B.append(b)
        if a in B:
            print(a)
            flag = 1
            break
        elif b in A:
            print(b)
            flag = 1
            break
    if flag == 0:
        print(-1)