import sys
from collections import deque
# sys.stdin.readline

n = int(sys.stdin.readline())

q = deque([i+1 for i in range(n)])

while True:
    if len(q) == 1:
        print(q[0])
        break

    q.popleft()
    if len(q) == 1:
        print(q[0])
        break

    q.append(q.popleft())
