import sys
from collections import Counter
# sys.stdin.readline()

sys.stdin.readline()
n = sys.stdin.readline().split()
sys.stdin.readline()
f = sys.stdin.readline().split()

c = Counter(n)

ret = ''

for i in f:
    print(c[i], end=' ')
