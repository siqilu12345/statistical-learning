import numpy as np
import mxnet as mx
from sklearn.externals import joblib
def getrawanswer(inputname,outputname,middleputname1,
                 middleputname2) :
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
    a=a*1000
    model_loaded = mx.model.FeedForward.load(middleputname1,6000)
    test_iter = mx.io.NDArrayIter(data=a)
    answer=model_loaded.predict(test_iter)
    ms = joblib.load(middleputname2)
    center=np.dot(answer,ms.cluster_centers_)
    '''
    center= ms.cluster_centers_[answer.argmax()]
    '''
    center = center + a[:, -2:]
    x1=center[:,0]/1000
    y1=center[:,1]/1000
    with open(outputname, 'a') as f:
        for i in range(len(label)):
            f.write(label[i] + ' ' + str(x1[i]) + ' ' + str(y1[i]) + '\n')
getrawanswer('/Users/siqilu/Desktop/testAnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/deeplearn/deeplearnAc',
             '/Users/siqilu/Desktop/Acluster/a')
getrawanswer('/Users/siqilu/Desktop/testBnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/deeplearn/deeplearnBc',
             '/Users/siqilu/Desktop/Bcluster/b')
getrawanswer('/Users/siqilu/Desktop/testCnum.txt',
             '/Users/siqilu/Desktop/rawanswer.txt',
             '/Users/siqilu/Desktop/deeplearn/deeplearnCc',
             '/Users/siqilu/Desktop/Ccluster/c')
with open('/Users/siqilu/Desktop/rawanswer.txt','r') as f :
    a=f.readlines()
for i in range(len(a)) :
    a[i]=a[i].split(' ')
a.sort(key=lambda x:int(x[0][1:]))
with open('/Users/siqilu/Desktop/answer.csv','w') as f :
    f.write('"TRIP_ID","LATITUDE","LONGITUDE"\n')
    for i in range(len(a)) :
        f.write('"'+str(a[i][0])+'"'+','+
                str(a[i][2][:-1])+','+str(a[i][1])+'\n')