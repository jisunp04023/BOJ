import sys

n = int(sys.stdin.readline())
dot = []

for i in range(n):
    s = sys.stdin.readline().split()
    dot.append([int(s[0]), int(s[1])])

dot.sort(key = lambda x : (x[1], x[0]))

for i in dot:
    print(str(i[0]) + ' ' + str(i[1]))
