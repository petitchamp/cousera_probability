XList = []
YList = []
XY = {}
for x in range(1,7):
    for y in range(1, 7):
        summation = x
        diff = x + y
        if summation in XY.keys():
            if diff in XY[summation].keys():
                XY[summation][diff] += 1
            else:
                XY[summation][diff] = 1
        else:
            XY[summation] = {}
            XY[summation][diff] = 1

print(XY)
#Px(4)
print(XY[3][3])