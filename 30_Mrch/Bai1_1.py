dictt={'name':'spiderman', 'description':'dead',2:'two'}
print(dictt)
dictt['age']='N/A'
print(dictt)
ans=input('Enter key: ')
ans2=input('Enter value: ')
dictt[ans]=ans2
print(dictt)
ans=input('Change something: ')
while ans not in dictt:
    ans=input('Change something: ')
ans2=input('Change what: ')
dictt[ans]=ans2
print(dictt)
ans=input('Delete?: ')
while ans not in dictt:
    ans=input('Delete?: ')
del dictt[ans]
print(dictt)