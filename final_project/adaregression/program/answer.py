import numpy as np
from sklearn.externals import joblib
def getrawanswer(inputname,outputname,middleputname1,middleputname2) :
    with open(inputname)as f:
        a = f.readlines()
    label = list()
    for i in range(len(a)):
        a[i] = a[i].split(' ')
        label.append(a[i][0])
        a[i] = a[i][1]
        a[i] = a[i][:-1]
        a[i] = a[i].split(',')
        if len(a[i]) >= 10:
            a[i] = a[i][0:10] + a[i][-10:]
        elif len(a[i]) >= 2:
            t = len(a[i])
            for j in range((20 - t) // 4):
                a[i].insert(2, a[i][0])
                a[i].insert(3, a[i][1])
            for j in range((20-len(a[i]))//2) :
                a[i].append(a[i][-2])
                a[i].append(a[i][-2])
    a = np.array(a)
    a = a.astype(np.float)
    n = 10
    b = [2 * i for i in range(n)]
    c = [2 * i + 1 for i in range(n)]
    trainx = a[:, b]
    trainy = a[:, c]
    aa = np.load(middleputname1)
    nn = 10
    bb = [2 * i for i in range(nn)]
    cc = [2 * i + 1 for i in range(nn)]
    ttrainx = aa[:, bb]
    ttrainy = aa[:, cc]
    xaverage = np.average(ttrainx)
    yaverage = np.average(ttrainy)
    trainx = (trainx - xaverage) * 10000
    trainy = (trainy - yaverage) * 10000
    clf = joblib.load(middleputname2)
    x1 = clf.predict(trainx)
    y1 = clf.predict(trainy)
    x1 = x1 / 10000 + xaverage
    y1 = y1 / 10000 + yaverage
    with open(outputname, 'a') as f:
        for i in range(len(label)):
            f.write(label[i] + ' ' + str(x1[i]) + ' ' + str(y1[i]) + '\n')
getrawanswer('/Users/siqilu/Desktop/testAnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/ada_Atrain.npy',
             '/Users/siqilu/Desktop/ada_Aresult/ada_Aresult.pkl')
getrawanswer('/Users/siqilu/Desktop/testBnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/ada_Btrain.npy',
             '/Users/siqilu/Desktop/ada_Bresult/ada_Bresult.pkl')
getrawanswer('/Users/siqilu/Desktop/testCnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/ada_Ctrain.npy',
             '/Users/siqilu/Desktop/ada_Cresult/ada_Cresult.pkl')