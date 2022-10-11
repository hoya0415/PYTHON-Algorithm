import sys
sys.stdin = open('./1773_input.txt')

N, C = map(int,input().split())
fire = [0] * (C+1)
for i in range(N):
    n = int(input())
    for j in range(1, C + 1):
        if j % n == 0 and fire[j] != 1:
            fire[j] = 1

print(sum(fire))