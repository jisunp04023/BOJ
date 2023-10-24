import sys
# sys.stdin.readline

n = int(sys.stdin.readline())
num = sys.stdin.readline().split()

num = set(num)
num = list(int(i) for i in num) # 리스트의 모든 요소를 int로 cast
num.sort()

print(*num) # 리스트의 요소 한 줄 출력
