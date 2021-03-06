library(splines)
a=runif(50,0,1)
a=sort(a)
u=rnorm(50,0,1)
x1=bs(a,degree = 1,intercept = TRUE)
obj1=lm(u~0+x1,data = as.data.frame(cbind(u,a)))
x2=bs(a,degree = 3,intercept = TRUE)
obj2=lm(u~0+x2,data = as.data.frame(cbind(u,a)))
x3=bs(a,df=6, knots = c(0.33,0.66),intercept = TRUE)
obj3=lm(u~0+x3,data = as.data.frame(cbind(u,a)))
x4=ns(a,df=6, knots = seq(0.1,0.9,0.16),intercept = TRUE)
obj4=lm(u~0+x4,data = as.data.frame(cbind(u,a)))
pwvar=function(x,obj)
{
  s=var(as.vector(obj$coefficients))
  co=s*x%*%t(x)
  diag(co)
}
pwv1=pwvar(x1,obj1)
pwv2=pwvar(x2,obj2)
pwv3=pwvar(x3,obj3)
pwv4=pwvar(x4,obj4)
ylim=range(c(pwv1,pwv2,pwv3,pwv4))
plot(a,pwvar(x1,obj1),type="l",col="orange",ylim = ylim)
lines(a,pwvar(x2,obj2),col="red")
lines(a,pwvar(x3,obj3),col="green")
lines(a,pwvar(x4,obj4),col="blue")

