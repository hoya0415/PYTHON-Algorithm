import sys
sys.stdin = open('./14888_input.txt')
from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
Y = [*a*['+'], *b*['-'], *c*['*'], *d*['%']]
max_v = -987654321
min_v = 987654321

for perm in permutations(Y, N-1):
    res = nums[0]
    i = 1
    for p in perm:
        if p == '+':
            res += nums[i]
        elif p == '-':
            res -= nums[i]
        elif p == '*':
            res *= nums[i]
        elif p == '%':
            if res < 0:
                res = abs(res) // nums[i]
                res *= -1
            else:
                res //= nums[i]
        i += 1
    if res > max_v:
        max_v = res
    if res < min_v:
        min_v = res

print(max_v)
print(min_v)
