import sys
sys.stdin = open('./1541_input.txt')

yes = list(input().split('-'))
ans = sum(map(int, yes[0].split('+')))

for y in yes[1:]:
    ans -= sum(map(int, y.split('+')))

print(ans)
