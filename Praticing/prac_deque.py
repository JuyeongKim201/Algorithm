from collections import deque

dq = deque([0,0,0,0,0])
print(dq)


def stackIn(i):
    dq.append(i)
    print("stackIn", i, "-> ", dq)

def stackOut():
    dq.pop()
    print("stackOut -> ", dq)

def queIn(i):
    dq.append(i)
    print("queIn", i, "-> ", dq)

def queOut():
    dq.popleft()
    print("queOut -> ", dq)

for i in range(1, 6):
    stackIn(i)

for i in range(1, 6):
    stackOut()

print('-----------')

for i in range(1, 6):
    queIn(i)

for i in range(1, 6):
    queOut()
