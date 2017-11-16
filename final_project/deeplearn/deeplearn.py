import numpy as np
import mxnet as mx
from sklearn.externals import joblib
def getlabel(train,result,inputname) :
    ms=joblib.load(inputname)
    label=ms.predict(result-train)
    return label
def neuralnet(inputname1,inputname2,outputname) :
    ms = joblib.load(inputname1)
    a = np.load(inputname2)
    train=a[:,:-2]*1000
    result=a[:,-2:]*1000
    data = mx.symbol.Variable('data')
    data = mx.sym.Flatten(data=data)
    fc1 = mx.sym.FullyConnected(data=data, name='fc1',
                                num_hidden=300)
    act1 = mx.sym.Activation(data=fc1, name='relu1',
                             act_type="relu")
    fc3 = mx.sym.FullyConnected(data=act1, name='fc3',
                                num_hidden=len(ms.cluster_centers_))
    mlp = mx.sym.SoftmaxOutput(data=fc3, name='softmax')
    model = mx.model.FeedForward(symbol=mlp,
        num_epoch=3000,
        learning_rate=0.1)
    train_iter = mx.io.NDArrayIter(data=train,
                                   label=getlabel(train[:,-2:],
                                                  result,
                                                  inputname1),
                                   batch_size=len(train)//300,
                                   shuffle=False)
    model.fit(X=train_iter)
    model.save(prefix=outputname,epoch=1000)
neuralnet('/Users/siqilu/Desktop/Acluster/a',
          '/Users/siqilu/Desktop/ada_Atrain.npy',
          '/Users/siqilu/Desktop/deeplearn/deeplearnA')
neuralnet('/Users/siqilu/Desktop/Bcluster/b',
          '/Users/siqilu/Desktop/ada_Btrain.npy',
          '/Users/siqilu/Desktop/deeplearn/deeplearnB')
neuralnet('/Users/siqilu/Desktop/Ccluster/c',
          '/Users/siqilu/Desktop/ada_Ctrain.npy',
          '/Users/siqilu/Desktop/deeplearn/deeplearnC')