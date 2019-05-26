st={'HP': 20,'DELL': 50,'MACBOOK': 12, 'ASUS': 30}
st_mon={'HP': 600,'DELL': 650,'MACBOOK': 12000, 'ASUS': 400, 'ACER': 350, 'TOSHIBA': 600, 'FUJITSU': 900, 'ALIENWARE': 1000}
#--------------------------CATALOG------------------------------
for i in st:
    print(i,':',st[i])
#-----------------------HIEN SO LUONG MAY THEO NG DUNG--------------------
ans=input('Enter computer model: ')
while ans.upper() not in st:
    ans=input('Enter computer model: ')    
print(st[ans.upper()])
#-----------------------THEM KEY VA VALUE MOI---------------------------
while True:
    ans=input('New computer model: ')
    ans2=int(input('No of computers: '))
    d=0
    ans=ans.upper()
    st[ans]=ans2
    for i in st:
        d+=st[i]
    print(d)
    ans=input('New computer model Y/N: ')
    if ans.upper() in ['NO','N']:
        break
#---------------------------THAY DOI GIA TRI KEY VA VALUE-----------------------------
while True:
    ans=input('Change storage Y/N: ')
    if ans in ['N','n','NO','no']:
        break
    ans=input('Change model: ')
    while ans.upper() not in st:
        ans=input('Change model: ')
    ans2=int(input('Change no: '))
    st[ans.upper()]=ans2

#---------------------------BANG GIA RELATED--------------------------------------
ans=input('Enter computer: ')
while ans.upper() not in st_mon:
    ans=input('Enter computer: ')
ans=ans.upper()
print('Money:', st_mon[ans])
#-------------------------------DAT DON HANG MUA MAY TINH------------------------------------------
ans=input('Enter item: ')
while ans.upper() not in st_mon:
    ans=input('Enter computer: ')
ans=ans.upper()
ans2=int(input('Enter no: '))
while ans2>st[ans]:
    ans2=int(input('Less no: '))
print('Money to pay: ', st_mon[ans]*ans2)
st[ans]-=ans2