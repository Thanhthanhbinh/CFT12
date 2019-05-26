
#BAI1_16Mrch
# lov=[]
# #func
# def pos(a):
#     whe=len(a)+1
#     while whe<0 or whe>len(a):
#         whe=int(input('Position of perference: '))
#     return int(whe)
# #mainloop
# while True:
#     ans=input('                  Enter or Quit: ')
#     if ans in ['c','C']:
#         l=input('What you love: ')
#         lov.append(l)
#     elif ans in ['r','R']:
#         if len(lov)>0:
#             print('Your love:')
#             for i in lov:
#                 print('                         ',i)
#         else:
#             print('No love')
#     elif ans in ['u','U']:
#         a=pos(lov)
#         cont=input('Change to: ')
#         lov[a-1]=cont
#     elif ans in ['d','D']:
#         a=pos(lov)
#         lov.pop(a-1)
#     elif ans in ['quit',"Quit"]:
#         print('                           END')
#         break
#BAI2_16Mrch
import random
while True:
    aa=''
    d=0
    tt=[]
    test=['milk','cat','dog','apple','market','exit','marbles','thunder']
    cho=random.randint(0,len(test)-1)
    while cho>len(test):
        cho=int(input('Choose word: '))
    a=list(test[cho])
    for i in range(len(a)): 
        b=random.randint(0,len(a)-1)
        while b in tt:
            b=random.randint(0,len(a)-1)
        tt.append(b)
        aa+=a[b]
    print("GUESS? ", aa)
    ans=input('Your answer: ')
    ans=ans.replace(' ','')
    mmmm=0
    if len(ans)!=len(test[cho]):
        print('wrong')
        mmmm=1
    k=list(ans)
    kk=list(test[cho])
    if mmmm!=1:
        for i in range(len(ans)):
            if k[i]==kk[i]:
                d+=1
        if d==len(test[cho]):
            print('correct')
        else:
            print('wrong')
            mmmm=1
    while mmmm==1:
        mmmm=0
        ans=input('Your answer: ')
        ans=ans.replace(' ','')
        if len(ans)!=len(test[cho]):
            print('wrong')
            mmmm=1
        k=list(ans)
        kk=list(test[cho])
        if mmmm!=1:
            for i in range(len(ans)):
                if k[i]==kk[i]:
                    d+=1
            if d==len(test[cho]):
                print('correct')
            else:
                print('wrong')
                mmmm=1 
