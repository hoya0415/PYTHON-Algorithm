import sys
sys.stdin = open('./1157_input.txt')

word = list(input().upper())
set_word = list(set(word))
word_cnt = []

for w in set_word:
    word_cnt.append(word.count(w))

if word_cnt.count(max(word_cnt)) > 1:
    print('?')
else:
    print(set_word[word_cnt.index(max(word_cnt))])