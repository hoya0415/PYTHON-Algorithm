import sys
sys.stdin = open('1259_input.txt')

while True:
    N = input()
    if N == '0':
        break

    flag = 0
    L = len(N)
    for i in range(L//2):
        if N[i] != N[L-i-1]:
            flag = 1
            break
    if flag == 0:
        print('yes')
    else:
        print('no')
