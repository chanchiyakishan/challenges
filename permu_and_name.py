from itertools import permutations
com = input().split(" ")
li = list(permutations(com[0], int(com[1])))
for i in range(len(li)):
    li[i] = "".join(li[i])
li.sort()
for x in li:
    print(*x, sep="")
