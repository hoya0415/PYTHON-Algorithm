import sys
sys.stdin = open('./1347_input.txt')
from collections import deque

N = int(input())
arr = list(input())
# 하, 좌, 상, 우
d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
x = y = k = min_x = min_y = max_x = max_y = 0
q = deque([(0, 0)])

for a in arr:
    if a == 'F':
        x += d[k][0]
        y += d[k][1]
        q.append((x, y))
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
    elif a == 'L':
        k = (k - 1) % 4
    elif a == 'R':
        k = (k + 1) % 4

X = max_x - min_x
Y = max_y - min_y

for i in range(X+1):
    for j in range(Y+1):
        if (i+min_x, j+min_y) in q:
            print('.', end='')
        else:
            print('#', end='')
    print()