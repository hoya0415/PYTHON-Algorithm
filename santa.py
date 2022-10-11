import sys
sys.stdin = open('santa_input.txt')

MIIS = lambda: map(int, input().split())
N, M = MIIS()
arr = list(list(MIIS()) for _ in range(N))

# 처음에 산타 위치 찾기(출발점), 착한 아이 수 구하기
good_children_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 3:
            start_i, start_j = i, j

        elif arr[i][j] == 0:
            good_children_cnt += 1



print(N, M)