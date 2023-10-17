# 문제: 일곱 난쟁이 (브론즈 1)
# itertools 활용하여 풀기
from itertools import *

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()
diff = sum(dwarf) - 100

catch = False

for permutation in permutations(dwarf, 2):
    if permutation[0] + permutation[1] == diff:
        dwarf.remove(permutation[0])
        dwarf.remove(permutation[1])
        break

for i in dwarf:
    print(i)


