# 문제: 요세푸스 문제 0 (실버 5)


'''
N = 7, K = 3 일 때,

1 2 * 4 5 6 7
<3>

1 2 * 4 5 * 7
<3 6>

1 * * 4 5 * 7
<3 6 2>

------
순환큐 느낌

K번 순서 당기기
    que[0] -> que[-1]

K번 당긴 후에 que[0] 아웃 - popleft()
-----
'''
from collections import deque

N, K = map(int, input().split())
people = deque([i for i in range(1, N+1)])
out = []

while len(people) > 0:
    # 순서 당기기
    for i in range(K-1):
        tmp = people[0]
        people.popleft()
        people.append(tmp)
    
    out.append(people[0])
    people.popleft()

prt = "<"
for i in range(len(out)):
    if i == len(out)-1:
        prt += f'{out[i]}>'
    else:
        prt += f'{out[i]}, '

print(prt)




