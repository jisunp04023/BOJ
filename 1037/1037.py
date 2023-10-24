import sys
# sys.stdin.readline

# a = n의 진짜 약수 (1, n 아님)
# n = a의 배수

N = int(sys.stdin.readline()) # 진짜 약수의 개수
num = sys.stdin.readline().split()
num = list(int(i) for i in num)

num.sort()

print(num[0] * num[-1])
