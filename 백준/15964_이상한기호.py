import sys
sys.stdin = open('15964_input.txt')


A, B = map(int, input().split())
print((A+B)*(A-B))