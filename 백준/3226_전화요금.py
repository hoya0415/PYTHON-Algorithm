import sys
sys.stdin = open('./3226_input.txt')

N = int(input())
arr = [input().split() for _ in range(N)]
res = 0
for ar in arr:
    a = int(ar[0][:2])
    b = int(ar[0][3:])
    c = int(ar[1])
    if 7 <= a < 19:
        if b+c > 59 and a+1 > 18:
             d = b + c - 60
             res += d * 5
             res += (c-d) * 10
        else:
            res += c * 10
    else:
        if b+c > 59 and 7 <= a+1 < 19:
            d = b+c - 60
            res += d * 10
            res += (c-d) * 5
        else:
            res += c * 5

print(res)

