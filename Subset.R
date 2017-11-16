rawdata=read.table('/Users/siqilu/Desktop/prostate.txt')
xtrain=rawdata[rawdata$train==TRUE,]
xtrain=xtrain[,-10]
xtest=rawdata[rawdata$train==FALSE,]
library(leaps)

obj=regsubsets(lpsa~.,xtrain)
objsum=summary(obj)
plot(objsum$rss,type = 'b')
plot(objsum$rsq,type = 'b')
plot(objsum$adjr2,type = 'b')
plot(objsum$bic,type = 'b')
n=which.min(objsum$bic)
k=coef(obj,n)
name=names(k)
yhat=as.matrix(xtest[name[-1]])%*%k[-1]+k[1]
testerror=1/30*t(xtest[,9]-yhat)%*%(xtest[,9]-yhat)
stderror=(var(x = (xtest[,9]-yhat)^2)/30)^0.5

objfw=regsubsets(lpsa~.,xtrain,method = 'forward')
objfwsum=summary(objfw)
plot(objfwsum$rss,type = 'b')
plot(objfwsum$rsq,type = 'b')
plot(objfwsum$adjr2,type = 'b')
plot(objfwsum$bic,type = 'b')
n=which.min(objfwsum$bic)
coef(objfw,n)

objbw=regsubsets(lpsa~.,xtrain,method = 'backward')
objbwsum=summary(objbw)
plot(objbwsum$rss,type = 'b')
plot(objbwsum$rsq,type = 'b')
plot(objbwsum$adjr2,type = 'b')
plot(objbwsum$bic,type = 'b')
n=which.min(objbwsum$bic)
coef(objbw,n)

objseq=regsubsets(lpsa~.,xtrain,method = 'seqrep')
objseqsum=summary(objseq)
plot(objseqsum$rss,type = 'b')
plot(objseqsum$rsq,type = 'b')
plot(objseqsum$adjr2,type = 'b')
plot(objseqsum$bic,type = 'b')
n=which.min(objseqsum$bic)
coef(objseq,n)


