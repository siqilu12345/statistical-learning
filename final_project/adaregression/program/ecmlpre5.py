import numpy as np
def adatraindata(inputname,outputname) :
    with open(inputname)as f:
        a = f.readlines()
    a=a[:len(a)//10]
    for i in range(len(a)):
        a[i] = a[i][:-1]
        a[i] = a[i].split(',')
        if len(a[i]) >= 12:
            a[i] = a[i][0:10] + a[i][-12:]
        elif len(a[i]) >= 2:
            t = len(a[i])
            for j in range((22 - t) // 4):
                a[i].insert(2, a[i][0])
                a[i].insert(3, a[i][1])
            for j in range((22-len(a[i]))//2) :
                a[i].append(a[i][-2])
                a[i].append(a[i][-2])
    b = np.array(a)
    b = b.astype(np.float)
    np.save(outputname, b)
adatraindata('/Users/siqilu/Desktop/AAnum.txt',
             '/Users/siqilu/Desktop/ada_Atrain')
adatraindata('/Users/siqilu/Desktop/BBnum.txt',
             '/Users/siqilu/Desktop/ada_Btrain')
adatraindata('/Users/siqilu/Desktop/CCnum.txt',
             '/Users/siqilu/Desktop/ada_Ctrain')