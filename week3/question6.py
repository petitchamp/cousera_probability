import itertools 
print len([ii for ii in itertools.permutations('1234') if ii[0] != '1' and ii[1] !='2' and ii[2] != '3' and ii[3] != '4'])

