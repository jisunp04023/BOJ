import sys
from itertools import combinations
# sys.stdin.readline()

n = int(sys.stdin.readline())
p = []
while n:
    n -= 1
    p.append(sys.stdin.readline().split())

p = list([int(i[0]), i[1], idx] for idx, i in enumerate(p))

p.sort(key = lambda x : (x[0], x[2]))

for j in list([i[0], i[1]] for i in p):
    print(str(j[0]) + ' ' + j[1])
