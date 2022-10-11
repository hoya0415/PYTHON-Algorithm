import sys
sys.stdin = open('./9933_input.txt')

N = int(input())
lst = []

for i in range(N):
    word = input()
    if list(reversed(word)) == list(word):
        print(len(word), word[len(word) // 2])
        break
    for l in lst:
        if list(reversed(l)) == list(word):
            print(len(l), l[len(l)//2])
            break
    lst.append(word)