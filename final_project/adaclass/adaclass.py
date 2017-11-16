import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib
def getlabel(train,result,inputname) :
    ms=joblib.load(inputname)
    label=ms.predict(result-train)
    return label
def adamodel(inputname1,inputname2,outputname) :
    a = np.load(inputname1)
    a=a[:len(a)//3]
    train=a[:,:-2]*1000
    result=a[:,-2:]*1000
    label=getlabel(train[:,-2:],result,inputname2)
    adacla=AdaBoostClassifier(base_estimator=DecisionTreeClassifier(
        max_depth=500
    ),
                              n_estimators=200)
    adacla.fit(train,label)
    joblib.dump(adacla, outputname)
adamodel('/Users/siqilu/Desktop/ada_Atrain.npy',
         '/Users/siqilu/Desktop/Acluster/a',
         '/Users/siqilu/Desktop/ada_Aresult/ada_Aresult.pkl',)
adamodel('/Users/siqilu/Desktop/ada_Btrain.npy',
         '/Users/siqilu/Desktop/Bcluster/b',
         '/Users/siqilu/Desktop/ada_Bresult/ada_Bresult.pkl')
adamodel('/Users/siqilu/Desktop/ada_Ctrain.npy',
         '/Users/siqilu/Desktop/Ccluster/c',
         '/Users/siqilu/Desktop/ada_Cresult/ada_Cresult.pkl')