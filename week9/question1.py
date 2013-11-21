__author__ = 'SONG Ke'

result = []
for die1 in range(1,7):
    for die2 in range(1,7):
        for die3 in range(1,7):
            avg = (die1+die2+die3)/3.0
            result.append(avg)

average = float(sum(result))/len(result)
avg = 0.0
sum = 0.0
for elem in result:
    sum += (elem - average)*(elem - average)

print (sum/len(result))
