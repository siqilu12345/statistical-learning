with open('/Users/siqilu/Desktop/test_A.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/testAnum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)
with open('/Users/siqilu/Desktop/test_B.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/testBnum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)
with open('/Users/siqilu/Desktop/test_C.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/testCnum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)