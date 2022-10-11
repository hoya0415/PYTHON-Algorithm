import sys
sys.stdin = open('./2309_input.txt')

from itertools import combinations

nanjangs = list(int(input()) for _ in range(9))
gap = sum(nanjangs) - 100

for comb in combinations(nanjangs, 2):
    if sum(comb) == gap:
        nanjangs.remove(comb[0])
        nanjangs.remove(comb[1])
        break

for nanjang in sorted(nanjangs):
    print(nanjang)
