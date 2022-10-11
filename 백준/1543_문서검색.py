import sys
sys.stdin = open('./1543_input.txt')

doc = input()
word = input()
i = cnt = 0

while doc.find(word, i) >= 0 and i < len(doc):
    cnt += 1
    i = doc.find(word, i) + len(word)

print(cnt)