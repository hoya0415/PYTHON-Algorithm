import sys
sys.stdin = open('./13458_input.txt')

N = int(input())
classes = list(map(int, input().split()))
B, C = map(int, input().split())
res = 0

for i in range(N):
    num = classes[i]
    if num < B:
        res += 1
        continue
    else:
        num -= B
        if num % C == 0:
            b = num // C + 1
        else:
            b = num // C + 2
    res += b

print(res)