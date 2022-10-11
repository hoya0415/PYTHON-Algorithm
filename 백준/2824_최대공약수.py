import sys, math
sys.stdin = open('./2824_input.txt')

N = int(input())
A = 1
N_list = list(map(int, input().split()))
for n in N_list:
    A *= n
M = int(input())
B = 1
M_list = list(map(int, input().split()))
for m in M_list:
    B *= m

res = str(math.gcd(A, B))
if len(res) > 9:
    print(res[-9:])
else:
    print(res)
