lit=['green','blue','yellow','red','black','purple']
print(*lit, sep=',')
ans=input('Enter color pos: ')
if ans.isdigit():
    if int(ans)>0 and int(ans)<=len(lit):
        lit.pop(int(ans)-1)
        print(*lit, sep=',')
    else:
        print('that does not exist')
if ans.isalpha():
    if ans in lit:
        lit.remove(ans)
        print(*lit, sep=',')

    else:
        print('that does not exist')