rawdata=read.table('/Users/siqilu/Desktop/prostate.txt')
xtrain=rawdata[rawdata$train==TRUE,]
xtest=rawdata[rawdata$train==FALSE,]
xtrain=xtrain[,-10]
obj=lm(formula = lpsa~.,data = xtrain)
summary(obj)
yhat=predict.lm(obj,xtest)
yhatsum=summary(yhat)
testerror=1/30*t(xtest[,9]-yhat)%*%(xtest[,9]-yhat)
stderror=(var(x = (xtest[,9]-yhat)^2)/30)^0.5

