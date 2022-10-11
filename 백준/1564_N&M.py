import sys
sys.stdin = open('1564_input.txt')
from itertools import permutations

N, M = map(int, input().split())
lst = list(range(1, N+1))

for perm in permutations(lst, M):
    print(*perm)