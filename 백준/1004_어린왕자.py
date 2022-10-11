import sys
sys.stdin = open('./1004_input.txt')

T = int(input())

for tc in range(T):
    SX, SY, EX, EY = map(int, input().split())
    N = int(input())
    cnt = 0
    lst = [list(map(int, input().split())) for _ in range(N)]
    for x, y, r in lst:
        d1 = (SX - x) ** 2 + (SY - y) ** 2
        d2 = (EX - x) ** 2 + (EY - y) ** 2
        rr = r ** 2

        if d1 < rr < d2 or d2 < rr < d1:
            cnt += 1
        print(cnt)
        # ly = y - r
        # ry = y + r
        # lx = x - r
        # rx = x + r
        # # 둘 다 들어있는 경우
        # if lx < SX < rx and ly < SY < ry and lx < EX < rx and ly < EY < ry:
        #     cnt = 0
        #     break
        # # 출발점만 들어있는 경우
        # elif lx < SX < rx and ly < SY < ry:
        #     cnt += 1
        # # 도착점만 들어있는 경우
        # elif lx < EX < rx and ly < EY < ry:
        #     cnt += 1

