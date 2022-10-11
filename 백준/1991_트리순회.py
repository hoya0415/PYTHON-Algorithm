import sys
sys.stdin = open('./1991_input.txt')

def order(a):
    global preorder, inorder, postorder
    if a != '.':
        preorder += a
        order(node[a][0])
        inorder += a
        order(node[a][1])
        postorder += a

N = int(input())
preorder = ''
inorder = ''
postorder = ''

node = {}

for _ in range(N):
    p, l, r = input().split()
    node[p] = [l, r]

order('A')

print(preorder)
print(inorder)
print(postorder)