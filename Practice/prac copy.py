from itertools import *
a = {1:[1,2], 2:[5,6], 3:[9,9]}
for i in permutations(a, 2):
    print(i)