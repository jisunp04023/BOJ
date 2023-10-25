import sys
# sys.stdin.readline

while True:
    s = sys.stdin.readline()[:-1]
    if s == '0':
        break

    if s == s[::-1]:
        print('yes')
    else:
        print('no')
