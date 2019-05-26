hih=[1,2,4,5,11,7,8]
def prin(a,b):
    for i in range(b):
        print(a[i])
prin(hih,len(hih))
while True:
    ans=int(input('Enter new high score: '))
    hih.append(ans)
    print('Rearrange: ')
    hih.sort(reverse=True)
    prin(hih,5)
    break
