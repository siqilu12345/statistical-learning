import numpy as np
import mxnet as mx
from sklearn.externals import joblib
inputname1='/Users/siqilu/Desktop/Bcluster/b'
inputname2='/Users/siqilu/Desktop/ada_Btrain.npy'
middleputname1='/Users/siqilu/Desktop/deeplearn/deeplearnBc'
def getlabel(train,result,inputname) :
    ms=joblib.load(inputname)
    label=ms.predict(result-train)
    return label
ms = joblib.load(inputname1)
a = np.load(inputname2)
train=a[:,:-2]*1000
result=a[:,-2:]*1000
train_iter = mx.io.NDArrayIter(data=train,
                               label=getlabel(train[:, -2:], result,
                                                          inputname1),
                               batch_size=len(train) // 300,
                               shuffle=False)
model_loaded = mx.model.FeedForward.load(middleputname1,6000)
print(model_loaded.score(train_iter))