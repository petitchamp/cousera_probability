# plato's flower
import itertools
perm = itertools.permutations('12345678')
all_permutaions = [ [ int(i) for i in ii ] for ii in perm  ] 
total_count = len(all_permutaions)
count = 0
for n in all_permutaions :	
	eightpos =n.index(8)
	if eightpos > 2 :
		n[eightpos]=0
		if n.index(max(n[:eightpos])) <= 2:
			count+=1
print count/float(total_count)
