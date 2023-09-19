from collections import deque

dq = deque([1,2,3,4,5,6])
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


stackIn(999)
stackOut()

queIn(999)
queOut()

