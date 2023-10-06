# 문제: 오븐 시계

h, m = map(int, input().split())
c = int(input())

m += c

while m >= 60:
    h += 1
    m -= 60

while h >= 24:
    h -= 24

print(h, m)
