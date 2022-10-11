import sys
sys.stdin = open('./13335_input.txt')
from collections import deque

N, W, L = map(int, input().split())
truks = deque(list(map(int, input().split())))
cnt = W
q = deque([0] * W)

while truks:
    q.popleft()
    if sum(q) + truks[0] <= L:
        truck = truks.popleft()
        q.append(truck)
    else:
        q.append(0)
    cnt += 1

print(cnt)