import sys
# sys.stdin.readline()

n = int(sys.stdin.readline())

i = 666
cnt = 1
while n != cnt:
    i += 1
    if '666' in str(i):
        cnt += 1
print(i)
