import sys
sys.stdin = open('./1010_input.txt')
from itertools import combinations

def check(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(check(M) // (check(M-N) * check(N)))