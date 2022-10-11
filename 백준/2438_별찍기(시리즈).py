import sys
sys.stdin = open('./2438_input.txt')

# 1
N = int(input())
for i in range(1, N+1):
    print('*' * i)

#2
N = int(input())
for i in range(1, N+1):
    print(' ' * (N-i)  + '*' * i)

#3
N = int(input())
for i in range(N, 0, -1):
    print('*' * i)

#4
N = int(input())
for i in range(N, 0, -1):
    print(' ' * (N-i)  + '*' * i)

#5
N = int(input())
for i in range(1, N+1):
    print(' ' * (N-i) + '*' * (2*i-1))

#6
N = int(input())
for i in range(N, 0, -1):
    print(' ' * (N-i) + '*' * (2*i-1))

#7
N = int(input())
for i in range(1, N):
    print(' ' * (N-i) + '*' * (2*i-1))
for i in range(N, 0, -1):
    print(' ' * (N-i) + '*' * (2*i-1))

#8
N = int(input())
for i in range(1, N+1):
    print('*' * (i) + ' ' * 2 *(N-i) + '*' * (i))
for i in range(N-1, 0, -1):
    print('*' * (i) + ' ' * 2 *(N-i) + '*' * (i))

#9
N = int(input())
for i in range(N, 1, -1):
    print(' ' * (N-i) + '*' * (2*i-1))
for i in range(1, N+1):
    print(' ' * (N-i) + '*' * (2*i-1))
