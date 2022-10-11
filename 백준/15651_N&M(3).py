import sys
sys.stdin = open('./15651_input.txt')
from itertools import product

N, M = map(int, input().split())
arr = list(range(1, N+1))

for pro in product(arr, repeat = M):
    print(*pro)




