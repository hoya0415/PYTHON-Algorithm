import sys
sys.stdin = open('2875_input.txt')


N, M, K = map(int, input().split())

N_max = N // 2
M_max = M
M_v = 0

if N_max > M_max:
    M_v = M_max
elif N_max < M_max:
    M_v = N_max
else:
    M_v = N_max

while K > 0 and M_v > 0:
    if N - (M_v * 2):
        K -= N - (M_v * 2)
        N -= N - (M_v * 2)
    elif M - M_v:
        K -= M - M_v
        M -= M - M_v
    else:
        N -= 1
        M_v -= 1
        K -= 1

print(M_v)

