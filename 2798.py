import sys
from itertools import combinations
# sys.stdin.readline

s = sys.stdin.readline().split()
n = int(s[0]) # 카드 개수
m = int(s[1]) # 가깝게 만들어야하는 target 숫자

s = sys.stdin.readline().split()
num = [int(i) for i in s]

add = []

for i in list(combinations(num, 3)):
    add.append(sum(i))

add.sort()

ret = 0

for i in add:
    if i <= m:
        ret = i
    else:
        break

print(ret)
