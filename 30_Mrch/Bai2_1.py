book={'name':'AHHHHHHH','publish year':'1999','characters':['a','a']}
film={'name':'OOf','publish year':'2000','characters':['b','b']}
al=[film,book]
#--------------------------------THAY LIST CO SAN-----------------------------------
print('Film before Book')
for i in al:
    ans=input('Add: ')
    ans2=input('More_add list seperate by space: ')
    ans2=ans2.split(' ')
    for j in ans2:
        if j == '':
            ans2.remove('')
    i[ans]=ans2
    for j in i:
        print(j, '-', i[j] )
#-------------------------------THEM VAO LIST CO SAN TRONG DICT---------------------------
print('Film befor book')
for j in al:
    ans=input('Enter: ')
    while ans not in j:
        ans=input('Enter: ')
    ans2=input('Content: ')
    j[ans].append(ans2)
    for i in j:
        print(i, '-', j[i] )
#------------------------------XOA TRONG LIST CO SAN TRONG DICT----------------------------
print('Film befor book')
for j in al:
    ans=input('Enter: ')
    while ans not in j:
        ans=input('Enter: ')
    ans2=int(input('What to delete: '))
    while ans2>len(j[ans]) or ans2<0:
        ans2=int(input('What to delete: '))
    j[ans].pop(ans2-1)
    for i in j:
        print(i, '-', j[i] )
#-----------------------------IN RA PHAN TU TRONG LIST CO SAN TRONG DICT---------------------------
print('film befor book')
for j in al:
    ans=input('Enter: ')
    while ans not in j:
         ans=input('Enter: ')
    ans2=int(input('Phan tu thu bao nhieu: '))
    while ans2>len(j[ans]) or ans2<0:
        ans2=int(input('Phan tu thu bao nhieu: '))
    print('Phan tu: ',j[ans][ans2-1])
#-----------------------------IN CAC PHAN TU TRONG LIST CO SAN MOT CACH DEP DE------------------------------
print('film befor book')
for j in al:
    for i in j:
        if type(boj[i])!=list:
            print(i, '-', j[i])
        else:
            print(i, '-', *j[i])