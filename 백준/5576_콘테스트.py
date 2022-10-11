import sys
sys.stdin = open('./5576_input.txt')

W = []
T = []

for i in range(20):
    if i < 10:
        w = int(input())
        W.append(w)
    else:
        t = int(input())
        T.append(t)

W = sorted(W, reverse=True)[:3]
T = sorted(T, reverse=True)[:3]

print(sum(W), sum(T))