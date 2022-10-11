import sys
sys.stdin = open('2615_input.txt')

def check(x, y, k):
    global cnt, ans

    for i in range(4):
        cnt = 1
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == k:
            global c_x_list, c_y_list
            c_x_list.append(x + 1)
            c_y_list.append(y + 1)
            c_x_list.append(nx + 1)
            c_y_list.append(ny + 1)
            cnt += 1
            cnt_check(nx, ny, i, k)
            if cnt == 5 and arr[x - dx[i]][y - dy[i]] != k:
                ans = k
                break
            else:
                c_x_list = []
                c_y_list = []

        elif ans > 0:
            break

def cnt_check(x, y, d, k):
    global cnt

    nx = x + dx[d]
    ny = y + dy[d]

    if ans > 0:
       return
    elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == k:
        c_x_list.append(nx+1)
        c_y_list.append(ny+1)
        cnt += 1
        cnt_check(nx, ny, d, k)


N = 19
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
cnt = 1
c_x_list = []
c_y_list = []

dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

for i in range(N):
    for j in range(N):
        if ans > 0:
            break
        if arr[i][j] == 1:
            check(i, j, 1)
            if ans > 0:
                break
        elif arr[i][j] == 2:
            check(i, j, 2)
            if ans > 0:
                break
print(c_x_list, c_y_list)


print(ans)
if ans > 0:
    if c_x_list[0] == c_x_list[1]:
        min_i = 0
        for z in range(4, -1, -1):
            if c_y_list[z] <= c_y_list[min_i]:
                min_i = z
    elif c_y_list[0] == c_y_list[1]:
        min_i = 0
        for z in range(5):
            if c_x_list[z] <= c_x_list[min_i]:
                min_i = z
    else:
        min_i = 0
        for z in range(4, -1, -1):
            if c_y_list[z] < c_y_list[min_i]:
                min_i = z
    print(c_x_list[min_i], c_y_list[min_i])
