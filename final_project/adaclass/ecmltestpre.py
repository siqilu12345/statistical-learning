with open('/Users/siqilu/Desktop/test.csv','r') as f :
    a=f.readlines()
b=a[1:]
with open('/Users/siqilu/Desktop/simpletest.txt','w') as g :
    for i in b :
        i=i.split('"')
        k=''
        for j in i :
            if j!='' and j!=',' :
                k=k+str(j)+' '
        g.write(k[:-1])
with open('/Users/siqilu/Desktop/simpletest.txt','r') as f:
    a=f.readlines()
for i in a :
    i=i.split(' ')
    if i[-1]=='\n' :
        if i[-3] == 'True':
            continue
        else:
            with open('/Users/siqilu/Desktop/test_' + i[1] + '.txt', 'a') as g:
                g.write(i[-2]+'\n')
    else :
        if i[-2] == 'True':
            continue
        else:
            with open('/Users/siqilu/Desktop/test_' + i[1] + '.txt', 'a') as g:
                g.write(i[-1]+'\n')
