lt = [2,3,5,2,4,5,4,3]
ans = int(input('Enter a number: '))
a = ""
if ans in lt:
    for i in range(len(lt)):
        if lt[i]==ans:
            a+=str(i)
            a+=" "
    print('Position(s): ', a)
else:
    print('Not in list')
#                                  SECOND ONE_CALCULATE SUM
print('Sum: ', sum(lt))
a=0
for i in lt:
    a+=i
print('Sum: ', a)