import sys
from collections import deque
input = sys.stdin.readline

a = deque()
a.append((1,2))
a.append((3,5))
a.append((2,1))
c = a.popleft()
print(c)
print(a)