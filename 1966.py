import sys
from pprint import pprint

# 문서의 개수 n, 궁금함 문서의 현재 위치 m
# 0-n까지 중요도

N = int(sys.stdin.readline())

while N:
    N -= 1
    s = sys.stdin.readline().split()
    n = int(s[0])
    m = int(s[1])

    imp = sys.stdin.readline().split()
    imp = list(int(i) for i in imp)

    printer = []

    for idx, i in enumerate(imp):
        printer.append([i, idx])

    ret = 1 # 출력 순서 저장

    while True:
        if printer[0][0] == max(i[0] for i in printer): # 현재 문서가 중요도 가장 높은 문서인 경우
            if printer[0][1] == m: # 현재 문서가 '순서가 궁금한 문서'인 경우
                break

            printer.pop(0) # 출력한 문서 pop
            ret += 1

        else: # 현재 문서보다 중요한 문서가 뒤에 있는 경우
            tmp = printer.pop(0) # 현재 문서 pop해서 맨 뒤 순서로 이동
            printer.append(tmp)

    print(ret)

