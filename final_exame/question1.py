
import itertools
perms = [ii for ii in itertools.permutations('1122345')]
count = 0
match_condition = True
for perm in perms:
    for i in range(len(perm)-1):
        if perm[i] == perm[i+1]:
            match_condition = False
            #print(perm)
            break

    if match_condition:
        print(perm)
        count += 1
    match_condition = True

print count

