# _*_ coding: utf-8 _*_

res = []
resNum = 0
for z in range(0, 28):
    res.append(0)
for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0,10):
            res[i + j +k] = res[i + j+k] + 1
            resNum += 1
print res
print resNum
