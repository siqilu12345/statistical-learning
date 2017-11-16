import numpy as np
import random
with open('/Users/siqilu/Desktop/train.csv','r') as f :
    a=f.readlines()
b=a[1:]
random.shuffle(b)
with open('/Users/siqilu/Desktop/simpletrain.txt','w') as g :
    for i in b[0:1200000] :
        i=i.split('"')
        k=''
        for j in i :
            if j!='' and j!=',' :
                k=k+str(j)+' '
        g.write(k[:-1])
with open('/Users/siqilu/Desktop/selftest.txt','w') as g :
    for i in b[1200000:] :
        i=i.split('"')
        k=''
        for j in i :
            if j!='' and j!=',' :
                k=k+str(j)+' '
        g.write(k[:-1])