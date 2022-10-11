import sys
sys.stdin = open('10703_input.txt')

R, S = map(int, input().split())
arr = [list(input()) for _ in range(R)]
min_move = R    # 땅과 유성의 거리가 가장 가까울 때의 거리를 저장할 변수.

# 땅과의 거리가 가장 가까울 때의 거리를 찾기
for i in range(S):
    cnt = 0
    X_cnt = 0
    for j in range(R-2, -1, -1):
        if arr[j][i] == '.':
            cnt += 1
            if cnt > min_move:
                break
        if arr[j][i] == 'X':
            X_cnt += 1
            break
        if arr[j][i] == '#':
            cnt = 0
            continue
    if X_cnt > 0 and cnt < min_move:
        min_move = cnt
    elif min_move == 1:
        break

# 그 거리만큼 아래로 이동시키기
for r in range(R-3, -1, -1):
    for c in range(S):
        if arr[r][c] == 'X':
            arr[r][c], arr[r+min_move][c] = arr[r+min_move][c], arr[r][c]

# 출력
for z in range(R):
    print(''.join(arr[z]))