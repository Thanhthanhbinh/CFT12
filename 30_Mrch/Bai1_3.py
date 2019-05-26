p1={'Huy':'','role': 'waiter','hours':12, 'salary':0.8}
p2={'Tung':'','role': 'cook','hours':24, 'salary':1.5}
p3={'M.Duc':'','role': 'manager','hours':20, 'salary':2}
name=''
people=[p1,p2,p3]
#--------------------------IN THONG TIN NGUOI MINH MUON = TEN-----------------------------
ans=input('Name: ')
def find_by_name(k,ans):
    while True:
        d=0
        for i in range(len(k)):
            if ans not in k[i]:
                d+=1
        if d==len(k):
            ans=input('Name: ')
        else:
            break
    a = 0
    for i in range(len(k)):
        if ans in k[i]:
            a = i
            break
    return a
print(people[find_by_name(people,ans)])
#-------------------------------THEM NG VAO DANH SACH---------------------------
anss=input('Add Y/N: ')
while anss in ['Yes','yes']:
    ans=input('Add name:')
    ans2=input('Add role: ')
    ans3=input('Add hours: ')
    while ans3.isalpha():
        ans3=input('Add hours: ')
    ans4=input('Add salary: ')
    while ans4.isalpha():
        ans4=input('Add salary: ')
    name={ans:'','role':ans2,'hours':int(ans3),'salary':int(ans4)}
    people.append(name)
    anss=input('Add more Y/N: ')
print(people)
#----------------------THAY DOI THONG TIN NGUOI TRONG DANH SACH----------------------------------
anss=input('Name: ')
changer=find_by_name(people,anss)
ans=input('Change role: ')
ans2=int(input('Change hours: '))
anss1=input('change name: ')
ans3=int(input('Change salary: '))
if ans!='':
    people[changer]['role']=ans
if ans2!='':
        people[changer]['hours']=ans2
if ans3!='':
        people[changer]['salary']=ans3
del people[changer][anss]
people[changer][anss1]=''
#---------------------------------IN MOI NG TREN MOT DONG----------------------------
for i in people:
    print(i)
#------------------------------------TINH LUONG THANG TUNG NG MOT-------------------------
for i in people:
    print(i['hours']*i['salary']*30)
#-----------------------------------TONG TIEN CHO NHAN VIEN MA NHA HANG CHI TRA-----------------------------
b=0
for i in people:
    a=i['hours']*i['salary']*30
    b+=a
print('So tien chi tra: ',b)



