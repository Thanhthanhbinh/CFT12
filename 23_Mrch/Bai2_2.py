ans=input("Enter list, elements seperated by ' ': ")
a=ans.split(',')
while ',' in a or '' in a:
    ans=input("Enter list, elements seperated by ' ': ")
    a=ans.split(',')
for i in range(len(a)):
        a[i]=int(a[i])
print('Your string: ', a)
print('sum of list: ', sum(a))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print('Even number: ', *b, sep=' ')