import sys
sys.stdin = open('2567_input.txt')

paper_num = int(input())
SIZE = 102
arr = [[0] * SIZE for _ in range(SIZE)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


for _ in range(paper_num):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] += 1

for r in range(1, SIZE):
    for c in range(1, SIZE):
        for z in range(4):
            if arr[r][c] >= 1:
                nr = r + dx[z]
                nc = c + dy[z]
                if 0 <= nr < SIZE and 0 <= nc < SIZE and arr[nr][nc] == 0:
                    cnt += 1

print(cnt)