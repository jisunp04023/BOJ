import sys
from itertools import combinations
# sys.stdin.readline

while True:
    s = sys.stdin.readline()
    if s == '0\n':
        break

    l = s.split()[1:]

    for i in list(combinations(l, 6)): # 조합
        print(*i) # list 한 줄 출력

    print('')
