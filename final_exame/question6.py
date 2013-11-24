XList = []
YList = []
XY = {}
for x in range(1,7):
    for y in range(1, 7):
        summation = x + y
        diff = abs(x - y)
        if summation in XY.keys():
            if diff in XY[summation].keys():
                XY[summation][diff] += 1
            else:
                XY[summation][diff] = 1
        else:
            XY[summation] = {}
            XY[summation][diff] = 1

print XY
#Px(4)
print XY[4]
#Fx,y(4,1)
print XY[4][1]
#Py(2)
count =0
for X in XY:
    if 2 in X.key():
        count += X[2]
#Py|x=4(0)
print X[4][0]