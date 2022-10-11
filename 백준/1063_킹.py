import sys
sys.stdin = open('./1063_input.txt')

K, S, N = list(input().split())
N = int(N)
K = [ord(K[0]) - 65, int(K[1]) - 1]
S = [ord(S[0]) - 65, int(S[1]) - 1]
chess = [[0] * (8) for _ in range(8)]
d = {'R':(1, 0), 'L':(-1, 0), 'T':(0, 1), 'B':(0, -1), 'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}

for _ in range(N):
    D = input()
    nkx = K[0] + d[D][0]
    nky = K[1] + d[D][1]
    if 0 <= nkx < 8 and 0 <= nky < 8:
        if [nkx, nky] == S:
            nsx = S[0] + d[D][0]
            nsy = S[1] + d[D][1]
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                S = [nsx, nsy]
                K = [nkx, nky]
        else:
            K = [nkx, nky]

print(chr(K[0] + 65) + str(K[1] + 1))
print(chr(S[0] + 65) + str(S[1] + 1))