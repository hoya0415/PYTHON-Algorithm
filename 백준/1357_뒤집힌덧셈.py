import sys
sys.stdin = open('./1357_input.txt')

X, Y = input().split()
print(int(str(int(X[::-1]) + int(Y[::-1]))[::-1]))