import sys
sys.stdin = open('./9093_input.txt')

T = int(input())
for _ in range(T):
    arr = list(input().split())
    for a in arr:
        print(''.join(reversed(a)), end=' ')
    print(sep='')