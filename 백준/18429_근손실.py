import sys
sys.stdin = open('./18429_input.txt')
from itertools import permutations

def check(lst):
    global cnt
    res = 0
    for i in range(N):
        res = res + lst[i] - K
        if res < 0:
            break
        if i == N-1:
            cnt += 1

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for perm in permutations(arr, N):
    check(perm)

print(cnt)