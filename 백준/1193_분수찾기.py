import sys
sys.stdin = open('./1193_input.txt')

X = int(input())
n = 0
for i in range(10000):
    n += i
    if X <= n:
        N = i
        break

a = N - (n-X)
b = (N+1) - a

if N % 2:
    print(f'{b}/{a}')
else:
    print(f'{a}/{b}')





