with open('/Users/siqilu/Desktop/call_A.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/Anum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)
with open('/Users/siqilu/Desktop/call_B.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/Bnum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)
with open('/Users/siqilu/Desktop/call_C.txt','r') as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/Cnum.txt','w') as g :
    for i in a :
        i=i.replace('[','')
        i=i.replace(']','')
        g.write(i)