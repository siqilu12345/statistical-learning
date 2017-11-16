se=function(x,df)
{
  std=vector()
  y=rep(0,times=100)
  for (i in 1:100)
  {
    y[i]=1
    z=smooth.spline(x=x,y=y,df=df)
    std=c(std,t(z$y)%*%z$y)
    y[i]=0
  }
  std
}
x=runif(100,0,1)
x=sort(x)
y0=sin(12*(x+0.2))/(x+0.2)
y=y0+rnorm(100,0,1)
obj1=smooth.spline(x,y,cv=TRUE)
plot(x,y)
lines(x,y0,col="red",lwd=2)
lines(obj1,col="green",lwd=2)
lines(x,obj1$y+2*se(x,obj1$df),col='green',lty=2,lwd=2)
lines(x,obj1$y-2*se(x,obj1$df),col='green',lty=2,lwd=2)
plot(x,y)
lines(x,y0,col="red",lwd=2)
obj2=smooth.spline(x,y,df =5)
lines(obj2,col="blue",lwd=2)
lines(x,obj2$y+2*se(x,obj2$df),col='blue',lty=2,lwd=2)
lines(x,obj2$y-2*se(x,obj2$df),col='blue',lty=2,lwd=2)
plot(x,y)
lines(x,y0,col="red",lwd=2)
obj3=smooth.spline(x,y,df =15)
lines(obj3,col="yellow",lwd=2)
lines(x,obj3$y+2*se(x,obj3$df),col='yellow',lty=2,lwd=2)
lines(x,obj3$y-2*se(x,obj3$df),col='yellow',lty=2,lwd=2)
cverr=vector()
epeerr=vector()
for (i in seq(5.1,20,0.1))
{
    obj4=smooth.spline(x,y,df=i)
    cverr=c(cverr,obj4$cv.crit)
    epeerr=c(epeerr,t(obj4$y-y0)%*%(obj4$y-y0))
}
ylim=range(c(cverr,(epeerr/100+1)))
plot(seq(5.1,20,0.1),cverr,type= "l",col='yellow', ylim = ylim)
lines(seq(5.1,20,0.1),(epeerr/100+1),type = "l",col='blue')

