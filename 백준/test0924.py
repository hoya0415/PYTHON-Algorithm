
def solution(n, m, x, y, r, c, k):
    def check(d, x, y):
        nx = x + dr[d][0]
        ny = y + dr[d][1]
        if 0 <= nx < n and 0 <= ny < m:
            return True
        return False

    def dfs(x, y, rst, cnt):
        if cnt == k:
            if (x, y) == (r, c):
                answer.append(rst)
            return
        if abs(x - r) + abs(y - c) <= k - cnt:
            for d in ['d', 'l', 'r', 'u']:
                nx = x + dr[d][0]
                ny = y + dr[d][1]
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx, ny, rst + d, cnt + 1)
        else:
            if x <= r and check('d', x, y):
                d = 'd'
            elif y >= c and check('l', x, y):
                d = 'l'
            elif y <= c and check('r', x, y):
                d = 'r'
            else:
                d = 'u'
            nx = x + dr[d][0]
            ny = y + dr[d][1]
            dfs(nx, ny, rst + d, cnt + 1)

    dr = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
    answer = []
    x, y, r, c = x- 1, y - 1, r - 1, c - 1
    if (abs(x - r) + abs(y - c)) % 2 != k % 2:
        return 'impossible'
    else:
        dfs(x, y, '', 0)

    return answer[0]

print(solution(3, 4, 2, 3,3, 1,  5))