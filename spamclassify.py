import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
with open('/Users/siqilu/Desktop/spam.txt') as f:
    a=np.loadtxt(f)
np.random.shuffle(a)
x=a[:,:-1]
y=a[:,-1]
xtrain=x[0:3065]
xtest=x[3065:]
ytrain=y[0:3065]
ytest=y[3065:]
tcf=DecisionTreeClassifier(max_leaf_nodes=1200)
bdt=AdaBoostClassifier(base_estimator=tcf,n_estimators=100,learning_rate=1)
bdt.fit(xtrain,ytrain)
print(bdt.score(xtrain,ytrain))
print(bdt.score(xtest,ytest))
