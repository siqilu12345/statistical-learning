import numpy as np
from sklearn.cluster import MeanShift,estimate_bandwidth
from sklearn.externals import joblib
def getlabel(inputname,outputname) :
    a = np.load(inputname)
    b = (a[:, -2:]-a[:,-4:-2])*1000
    bandw = estimate_bandwidth(b, quantile=0.1, n_samples=50000)
    ms = MeanShift(bandwidth=bandw, bin_seeding=True, min_bin_freq=5)
    ms.fit(b)
    joblib.dump(ms, outputname)
getlabel('/Users/siqilu/Desktop/ada_Atrain.npy',
         '/Users/siqilu/Desktop/Acluster/a')
getlabel('/Users/siqilu/Desktop/ada_Btrain.npy',
         '/Users/siqilu/Desktop/Bcluster/b')
getlabel('/Users/siqilu/Desktop/ada_Ctrain.npy',
         '/Users/siqilu/Desktop/Ccluster/c')