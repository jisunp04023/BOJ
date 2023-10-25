import sys
# sys.stdin.readline

sys.stdin.readline()
l = set(sys.stdin.readline().split()) # 중복 제거로 시간초과 해결
sys.stdin.readline()
f = sys.stdin.readline().split()

ret = ''
for i in f:
    if i in l:
        ret += '1\n'
    else:
        ret += '0\n'
print(ret)
