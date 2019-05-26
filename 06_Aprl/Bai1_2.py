import random
#--------------------------TEXT BASED ADVENTURE----------------------------
char={'name':'a', 'atk':4, 'def':3, 'hp':10, 'inventory':['food'], 'gold':8, 'lvl':2}
skill1={'name':'Tackle', 'atk':5, 'lvl':1, 'hr': 0.3}
skill2={'name':'Quick attack', 'atk':3, 'lvl':2, 'hr': 0.5}
skill3={'name':'Strong Kick', 'atk':9, 'lvl':4, 'hr': 0.2}
skill=[skill1,skill2,skill3]
#---------------------------BEGIN MATCH-------------------------------------------
print('---------------THIS IS YOU-----------------')
for i in char:
    print('                 ',i, ':', char[i])
print('---------------BEGAN BATTLE----------------')
print('                 SKILL SET')
for i in skill:
    print(i['name'],'-', i['atk'])
#--------------------------COMBAT----------------------------------
ans=input('Attack: ')
d=0
for i in skill:
    if ans !=i['name']:
        d+=1
while d==len(skill):
    ans=input('Attack: ')
    d=0
    for i in skill:
        if ans !=i['name']:
            d+=1
for i in skill:
    if ans ==i['name']:
        choosen=i
if char['lvl']<choosen['lvl']:
    print('Not enough level')
else:
    a=random.uniform(0.0,1.0)
    if a<=choosen['hr']:

        print('Cause:', choosen['atk'])
    else:
        print('Miss')
    



