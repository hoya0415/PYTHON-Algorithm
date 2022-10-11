import sys
sys.stdin = open('./1331_input.txt')

arr = [[0] * 6 for _ in range(6)]

for i in range(36):
    inp = input()
    x = ord(inp[0]) - 65
    y = int(inp[1]) - 1
    if i == 0:
        sx, sy = px, py = x, y
    if arr[x][y] == 0:
        arr[x][y] = 1
        if abs(px - x) == 2 and abs(py - y) == 1 or abs(px - x) == 1 and abs(py - y) == 2:
            px, py = x, y
            if i == 35:
                if abs(sx - x) == 2 and abs(sy - y) == 1 or abs(sx - x) == 1 and abs(sy - y) == 2:
                    res = 'Valid'
                else:
                    res = 'Invalid'
        elif i == 0:
            pass
        else:
            res = 'Invalid'
            break
    else:
        res = 'Invalid'
        break

print(res)