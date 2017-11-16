rawdata=read.table('/Users/siqilu/Desktop/prostate.txt')
xtrain=rawdata[rawdata$train==TRUE,]
xtrain=xtrain[,-10]
xtest=rawdata[rawdata$train==FALSE,]
x=as.matrix(xtrain)[,1:8]
y=xtrain[,9]
library(glmnet)
lambdalist=10^(seq(5,-5,-0.2))
obj=glmnet(x,y,alpha = 0, lambda = lambdalist)
objsum=summary(obj)
cv=cv.glmnet(x,y,alpha=0,lambda = lambdalist)
plot(cv)
stderror=mean(cv$cvsd)
lambdachoose=cv$lambda.min
n=which(cv$lambda==lambdachoose)
k=coef(obj)[,n]
yhat=predict.glmnet(obj,newx=as.matrix(xtest[,-c(9,10)]),s = lambdachoose)
testerror=1/30*t(xtest[,9]-yhat)%*%(xtest[,9]-yhat)
stderrortest=(var(x = (xtest[,9]-yhat)^2)/30)^0.5

