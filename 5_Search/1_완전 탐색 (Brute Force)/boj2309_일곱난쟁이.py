# 문제: 일곱 난쟁이 (브론즈 1)
# itertools 모듈 없이 풀기

dwarf = []
for i in range(9):
    dwarf.append(int(input()))
dwarf.sort()

diff = sum(dwarf) - 100
catch = False

for i in range(9):
    if catch:
        break

    for j in range(9):
        if i == j:
            break

        if dwarf[i]+dwarf[j] == diff:
            dwarf.remove(dwarf[i])
            dwarf.remove(dwarf[j])
            catch = True
            break

for i in dwarf:
    print(i)
