import sys
sys.stdin = open('11315_input.txt')

def omok():
    for x in range(N):
        for y in range(N):
            # arr를 돌면서 'o'를 발견하면
            if arr[x][y] == 'o':
                # 우, 우하, 하, 좌하 탐색
                for k in range(4):
                    cnt = 1
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 만약 해당방향에 벽이 아니고 'o'가 있으면
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                        cnt += 1
                        rx = nx + dx[k]
                        ry = ny + dy[k]
                        # 그쪽 방향에 'o'가 몇개 있는 지 탐색
                        while 0 <= rx < N and 0 <= ry < N and arr[rx][ry] == 'o':
                            cnt += 1
                            rx += dx[k]
                            ry += dy[k]
                    # 탐색 후 cnt가 5면 'YES'리턴
                    if cnt == 5:
                        return 'YES'
    # 모든 방향 탐색 후 발견 못 하면 'NO' 리턴
    return 'NO'


# 우, 우하, 하, 좌하 탐색
dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print('#{} {}'.format(tc, omok()))

