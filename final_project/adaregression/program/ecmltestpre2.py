with open('/Users/siqilu/Desktop/simpletest.txt','r') as f:
    a=f.readlines()
for i in a :
    i=i.split(' ')
    if i[-1]=='\n' :
        if i[-3] == 'True':
            continue
        else:
            with open('/Users/siqilu/Desktop/test_' + i[1] + '.txt', 'a') as g:
                g.write(i[0]+' '+i[-2]+'\n')
    else :
        if i[-2] == 'True':
            continue
        else:
            with open('/Users/siqilu/Desktop/test_' + i[1] + '.txt', 'a') as g:
                g.write(i[0]+' '+i[-1]+'\n')
