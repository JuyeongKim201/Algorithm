
a = 1

def plus_global():
    global a
    a += 1
    print(a)

def plus():
    a += 1
    print(a)

plus_global()
plus()