# a = 0.38534124
a = 0.6
result = []

while True:
    if a*2 > 1:
        a = a*2 - 1
        result.append(1)
    elif a*2 == 1:
        result.append(1)
        break
    else:
        a = a*2
        result.append(0)

print(result)

sum = 0
for i in range(1, len(result)+1):
    if result[i-1] == 1:
        sum += 1/(2**i)

print(sum)

a=2**32
print(a/8000000)

