rawdata=read.table('/Users/siqilu/Desktop/prostate.txt')
xtrain=rawdata[rawdata$train==TRUE,]
xtrain=xtrain[,-10]
xtest=rawdata[rawdata$train==FALSE,]
x=as.matrix(xtrain)[,1:8]
y=xtrain[,9]
ls=lm(formula = lpsa~., data = xtrain)
lambdamax=sum(abs(ls$coefficients))
library(glmnet)
lambdalist=seq(from = 0, to = lambdamax, length.out = 200)
obj=glmnet(x,y,alpha = 1, lambda = lambdalist)
objsum=summary(obj)
cv=cv.glmnet(x,y,alpha=1,lambda = lambdalist)
plot(cv)
stderror=mean(cv$cvsd)
lambdachoose=cv$lambda.1se
n=which(cv$lambda==lambdachoose)
k=coef(obj)[,n]
yhat=predict.glmnet(obj,newx=as.matrix(xtest[,-c(9,10)]),s = lambdachoose)
testerror=1/30*t(xtest[,9]-yhat)%*%(xtest[,9]-yhat)
stderrortest=(var(x = (xtest[,9]-yhat)^2)/30)^0.5

