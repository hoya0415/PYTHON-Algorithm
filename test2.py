import sys
sys.stdin = open('test2.txt')

#1 3

#2 13

#3 18

#4 22

#5 22

def find(M_num, h):
    m = M_list[M_num]
    c = C_list[M_num]
    res = abs(h[0] - m[0]) + abs(h[1] - m[1])
    res += abs(c[0] - m[0]) + abs(c[1] - m[1])

    return res

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    M_list = [(0, 0), (0, 0), (0, 0), (0, 0)]
    C_list = [(0, 0), (0, 0), (0, 0), (0, 0)]

     # 몬스터 개수, 위치 알아치기
    M = 0
    for i in range(N) :
        for j in range(N):
            if arr[i][j] > M:
                M = arr[i][j]
            if arr[i][j] > 0:
                M_list[arr[i][j] - 1] = (i, j)
            elif arr[i][j] < 0:
                C_list[abs(arr[i][j]) - 1] = (i, j)


    min_cnt = 987654321
    if M == 1:
        h = (0, 0)
        res = find(0, h)
        min_cnt = res
    elif M == 2:
        for k in range(2):
            h = (0, 0)
            cnt = 0
            cnt += find(k, h)
            h = C_list[k]
            cnt += find((k+1) % 2, h)
            if cnt < min_cnt:
                min_cnt = cnt
    elif M == 3:
        for k in range(M):
            h = (0, 0)
            cnt = 0
            for a in range(M):
                cnt += find(a % M, h)
                h = C_list[a]
            if cnt < min_cnt:
                min_cnt = cnt
            h = (0, 0)
            cnt = 0
            for b in range(M, -1, -1):
                cnt += find(b % M, h)
                h = C_list[b]
            if cnt < min_cnt:
                min_cnt = cnt


    print(f'#{tc} {min_cnt}')