from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_gaussian_quantiles
x, y = make_gaussian_quantiles(n_samples=1000, n_features=10,
                                 n_classes=2)
bdt=AdaBoostClassifier(n_estimators=200,learning_rate=1)
bdt.fit(x,y)
print(bdt.score(x,y))
x1,y1=make_gaussian_quantiles(n_samples=2000, n_features=10,
                                 n_classes=2)
print(bdt.score(x1,y1))