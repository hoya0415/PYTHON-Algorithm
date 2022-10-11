import sys
sys.stdin = open('./21736_input.txt')
import time
from collections import deque

starttime = time.time()

N, M = map(int, input().split())

cam = []
visited = [[0] * M for _ in range(N)]

# 좌, 우, 상, 하
d = [ (0, -1), (0, 1),(-1, 0), (1, 0)]
p_cnt = 0
x_cnt = 0

for i in range(N):
    tmp = input()
    cam.append(tmp)
    for j in range(M):
        if tmp[j] == 'I':
            q = deque([(i, j)])
        if tmp[j] == 'X':
            visited[i][j] = 1
            x_cnt += 1
        if tmp[j] == 'P':
            p_cnt += 1

people = 0
if x_cnt == 0:
    people = p_cnt
else:
    while q:
        s = q.popleft()
        visited[s[0]][s[1]] = 1

        for i in range(4):
            new_x = s[0]+d[i][0]
            new_y = s[1]+d[i][1]
            if 0 <= new_x < N and 0 <= new_y < M:
                if visited[new_x][new_y] == 0 and (new_x, new_y) not in q:
                    if cam[new_x][new_y] == 'P':
                        people += 1
                        if people >= p_cnt:
                            break
                    q.append((new_x, new_y))
        if people >= p_cnt:
            break


if people == 0:
    print('TT')
else:
    print(people)

print(visited, x_cnt, p_cnt, s)

end = time.time()
print(end - starttime)