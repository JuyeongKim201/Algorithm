# 문제: 수 정렬하기 (브론즈 2)

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort()

for i in nums:
    print(i)

