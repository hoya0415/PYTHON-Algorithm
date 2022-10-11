import sys
sys.stdin = open('2563_input.txt')

paper_num = int(input())
SIZE = 100
arr = [[0] * SIZE for _ in range(SIZE)]

result = paper_num * 10 * 10

for _ in range(paper_num):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] += 1

for r in range(SIZE):
    for c in range(SIZE):
        for z in range(2, paper_num + 1):
            if arr[r][c] == z:
                result -= z-1

print(result)