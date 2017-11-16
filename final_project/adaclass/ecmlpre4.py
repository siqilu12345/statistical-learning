with open('/Users/siqilu/Desktop/Anum.txt')as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/AAnum.txt','w')as f :
    for i in a :
        if i!='\n' :
            f.write(i)
with open('/Users/siqilu/Desktop/Bnum.txt')as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/BBnum.txt','w')as f :
    for i in a :
        if i!='\n' :
            f.write(i)
with open('/Users/siqilu/Desktop/Cnum.txt')as f :
    a=f.readlines()
with open('/Users/siqilu/Desktop/CCnum.txt','w')as f :
    for i in a :
        if i!='\n' :
            f.write(i)
