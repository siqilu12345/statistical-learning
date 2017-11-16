with open('/Users/siqilu/Desktop/rawanswer.txt','r') as f :
    a=f.readlines()
for i in range(len(a)) :
    a[i]=a[i].split(' ')
a.sort(key=lambda x:int(x[0][1:]))
with open('/Users/siqilu/Desktop/answer.csv','w') as f :
    f.write('"TRIP_ID","LATITUDE","LONGITUDE"\n')
    for i in range(len(a)) :
        f.write('"'+str(a[i][0])+'"'+','+
                str(a[i][2][:-1])+','+str(a[i][1])+'\n')
