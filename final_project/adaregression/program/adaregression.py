import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.externals import joblib
def adamodel(inputname,outputname) :
    a = np.load(inputname)
    n = 10
    b = [2 * i for i in range(n)]
    c = [2 * i + 1 for i in range(n)]
    trainx = a[:, b]
    trainy = a[:, c]
    resultx = a[:, -2]
    resulty = a[:, -1]
    xaverage = np.average(trainx)
    yaverage = np.average(trainy)
    trainx = (trainx - xaverage) * 10000
    resultx = (resultx - xaverage) * 10000
    trainy = (trainy - yaverage) * 10000
    resulty = (resulty - yaverage) * 10000
    train = np.concatenate((trainx, trainy))
    result = np.concatenate((resultx, resulty))
    adareg = AdaBoostRegressor(
        base_estimator=DecisionTreeRegressor(max_depth=500),
        n_estimators=30,
        loss='square')
    adareg.fit(train, result)
    joblib.dump(adareg, outputname)
adamodel('/Users/siqilu/Desktop/ada_Atrain.npy',
         '/Users/siqilu/Desktop/ada_Aresult/ada_Aresult.pkl')
adamodel('/Users/siqilu/Desktop/ada_Btrain.npy',
         '/Users/siqilu/Desktop/ada_Bresult/ada_Bresult.pkl')
adamodel('/Users/siqilu/Desktop/ada_Ctrain.npy',
         '/Users/siqilu/Desktop/ada_Cresult/ada_Cresult.pkl')