import sys
sys.stdin = open('./2851_input.txt')

res = 0

for i in range(10):
    n = int(input())
    res += n
    if res == 100:
        break
    elif res > 100:
        if abs(res-100) <= abs(res-100-n):
            break
        else:
            res -= n
            break

print(res)