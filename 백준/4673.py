N = 10000
self = [0] * (N+1)

for i in range(1, N + 1):
    if i + sum(map(int, str(i))) > N:
        continue
    self[i + sum(map(int, str(i)))] = 1

for i in range(1, N+1):
    if not self[i]:
        print(i)