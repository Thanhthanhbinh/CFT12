import random
time=0
no=0
while True:
    time+=1
    maze={'x':20, 'y':20}
    #cooP=PLAYER
    #cooW=WALL
    #cooK=KEY(S)
    #cooE=EXIT
    #-------------------------------COORDINANCES SETUP------------------------------
    cooKs=[]
    cooWs=[]
    cooP={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}#cooP
    for i in range(time):
        cooK={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}#cooK
        while cooK['x']==cooP['x'] and cooK['y']==cooP['y']:#cooK cri
            cooK={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}
        cooKs.append(cooK)
    cooE={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}#cooE
    while cooE['x'] in [cooK['x'], cooP['x']] and cooE['y'] in [cooK['y'], cooP['y']]:#cooE cri
        cooE={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}
    for i in range(time+9):
        cooW={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}#cooW
        while cooW['x'] in [cooK['x'], cooP['x'], cooE['x']] and cooE['y'] in [cooK['y'], cooP['y'],cooE['y']]:#cooW cri
            cooW={'x':random.randint(1,maze['x']), 'y':random.randint(1,maze['y'])}
        cooWs.append(cooW)
    a=0
    Kx=[]
    Wx=[]
    Wy=[]
    for i in cooKs:
        Kx.append(i['x'])
    for i in cooWs:
        Kx.append(i['x'])
        Wx.append(i['x'])
    for i in cooWs:
        Wy.append(i['y'])
    #---------------------PRINT FUNCTION-----------------
    def pin():
        print(cooE,' E')
        for i in cooKs:
            print(i,' K')
        print(cooP,' P')
        print(cooW,' w')
        print(Kx)
    #------------------WASD----------------------------
    def forward(p):#D
        if p['y'] != maze['y']:
            p['y']+=1
    def backward(p):#A
        if p['y'] != 1:
            p['y']-=1
    def up(p):#W
        if p['x'] !=1:
            p['x']-=1
    def down(p):#S
        if p['x'] !=maze['x']:
            p['x']+=1
    pin()
    #---------------------------------------MAINLOOP()1-----------------------------------------------------------
    while True:
        row=' '
        #---------------------SET UP MAP--------------------
        for j in range(1,maze['x']+1):#XET DONG
            if j not in [cooE['x'],cooP['x']] and j not in Kx:#NEU KO CO DIEM THUOC DONG
                for k in range(1,maze['y']+1):
                    row+='- '
                print(row)
                row=' '
            else:#NEU CO DIEM THUOC DONG
                for k in range(1,maze['y']+1):
                    check=0
                    if k ==cooE['y'] and cooE['x']==j:#TAI [I,J] VS J CUA E
                        row+='E '
                        check+=1
                    if k==cooP['y'] and cooP['x']==j:#TAI [I,J] VS J CUA P
                        row+='P '
                        check+=1
                    for h in cooWs:#Tai [I,J] VS J CUA CAC W
                        if k==h['y'] and h['x']==j:
                            row+='W '
                            check+=1
                    for h in cooKs:#Tai [I,J] VS J CUA CAC K
                        if k==h['y'] and h['x']==j:
                            row+='K '
                            check+=1
                    if check==0:#TAI [I,J] VS J KO CO GI
                        row+='- '
                print(row)
                row=' '
        if a==1:#--------------------CHECK KEY------------------------
            break
        #-----------------MOVEMENT----------------------
        ans=input('MOVE: ')
        if ans in ['D','d']:
            forward(cooP)
            for i in cooWs:
                if cooP['x']==i['x'] and cooP['y']==i['y']:
                    backward(cooP)
        if ans in ['A','a']:
            backward(cooP)
            for i in cooWs:
                if cooP['x']==i['x'] and cooP['y']==i['y']:
                    forward(cooP)
        if ans in ['w','W']:
            up(cooP)
            for i in cooWs:
                if cooP['x']==i['x'] and cooP['y']==i['y']:
                    down(cooP)
        if ans in ['S','s']:
            down(cooP)
            for i in cooWs:
                if cooP['x']==i['x'] and cooP['y']==i['y']:
                    up(cooP)
        #----------------CHECK POSITION-------------
        for i in cooKs:
            if cooP['x']==i['x'] and cooP['y']==i['y']:
                i['x']=0
                no+=1
                print('FOUND KEY')
        if cooP['x']==cooE['x'] and cooP['y']==cooE['y']:
            if no==time:
                a=1
                cooE['x']=0
                no=0
            else:
                print('FIND KEY')
    print('YOU MADE IT')



    

