qz1={'q1q':['A.2','B.3','C.4'], 'q1a':'A','q1':'1+1=2'}
qz2={'q1':'Why did the chiken cross the road?','q1q':["A.to get to the idiot's house",'B.to get to the other side'],'q1a':"A"}
qz3={'q1':'Knock knock!','q1q':["A.who's there?",'B.stop this'],'q1a':'A'}
qz4={'q1':'The chiken','q1q':['A.no','B.haha'],'q1a':'B'}
quiz=[qz1,qz2,qz3,qz4]
d=0
for i in quiz:
    print(i['q1'])
    for j in i['q1q']:
        print(j)
    ans=input('Answer: ')
    ans=ans.upper()
    if ans==i['q1a']:
        d+=1
        print('Correct')
print(d)
d=len(quiz)/d
print(len(quiz))
d=100/d
print('points: ',round(d), '%')
