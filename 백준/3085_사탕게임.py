import sys
sys.stdin = open('./3085_input.txt')

def check(arr, x, y, c, pull):
    flag = 0
    if x > 0:
        if arr[x - 1][y] == c:
            flag = 1
            pull = 0
    if x < N - 1 and flag == 0:
        if arr[x + 1][y] == c:
            flag = 1
            pull = 0
    if 0 < y and flag == 0:
        if arr[x][y - 1] == c:
            flag = 1
            pull = 1
    return flag, pull

N = int(input())
x_arr = []
y_arr = [[] for _ in range(N)]
candy = ['C', 'P', 'Z', 'Y']
res = 0

for i in range(N):
    y_lst = list(input())
    x_arr.append(y_lst)
    for j in range(N):
        y_arr[j].append(y_lst[j])

for c in candy:
    for i in range(N):
        if x_arr[i].count(c) >= res or y_arr[i].count(c) >= res:
            x_cnt = y_cnt = x_flag = y_flag = x_pull = y_pull = 0
            y_flag_index = x_flag_index = -1
            for j in range(N):
                # 가로 검사
                if x_arr[i][j] == c:
                    x_cnt += 1
                else:
                    if x_flag == 0:
                        if j > 0:
                            if x_arr[i][j-1] != c:
                                x_cnt = 0
                    else:
                        x_cnt = j - x_flag_index - 1

                    x_flag, x_pull = check(x_arr, i, j, c, x_pull)
                    if x_flag == 0:
                        x_cnt = 0
                    else:
                        x_flag_index = j
                        if x_pull:
                            x_cnt = 1
                        else:
                            x_cnt += x_flag

                # 세로 검사
                if y_arr[i][j] == c:
                    y_cnt += 1
                else:
                    if y_flag == 0:
                        if j > 0:
                            if y_arr[i][j-1] != c:
                                y_cnt = 0
                    else:
                        y_cnt = j - y_flag_index - 1

                    y_flag, y_pull = check(y_arr, i, j, c, y_pull)
                    if y_flag == 0:
                        y_cnt = 0
                    else:
                        y_flag_index = j
                        if y_pull:
                            y_cnt = 1
                        else:
                            y_cnt += y_flag

                if max(x_cnt, y_cnt) > res:
                    res = max(x_cnt, y_cnt)
            if res == N:
               break
    if res == N:
        break

print(res)

