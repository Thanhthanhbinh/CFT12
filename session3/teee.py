#BAI_3_4
# from random import randint
# num=randint(0, 100)
# if num <30:
#     print('rainy')
# elif num in range(30,60):
#     print('cloudy')
# else:
#     print('sunny')
#BAI_6
# a=float(input('enter a: '))
# b=float(input('enter b: '))
# c=float(input('enter c: '))
# delta= (b**2)-4*a*c
# if delta<0:
#     print('No')
# elif delta==0:
#     print(round(-b/(2*a)),round(b/(2*a)) )
# else:
#     print('nghiem1: ', round(((-b-(delta**0.5))/2*a)))
#     print('nghiem2: ', round(((-b+(delta**0.5))/2*a)))
#AI01_23Mrch
# from turtle import *
# lit=['green','blue','yellow','red','black','purple']
# shape('turtle')
# for i in lit:
#     color(i)
#     forward(100)
#     left(60)
# mainloop()
# print(*lit, sep=',')
# ans=input('Enter color pos: ')
# if ans.isdigit():
#     if int(ans)>0 and int(ans)<=len(lit):
#         lit.pop(int(ans)-1)
#         print(*lit, sep=',')
#     else:
#         print('that does not exist')
# if ans.isalpha():
#     if ans in lit:
#         lit.remove(ans)
#         print(*lit, sep=',')

#     else:
#         print('that does not exist')
#BAI02_23Mrch
#lt = [2,3,5,2,4,5,4,3]
# ans = int(input('Enter a number: '))
# a = ""
# if ans in lt:
#     for i in range(len(lt)):
#         if lt[i]==ans:
#             a+=str(i)
#             a+=" "
#     print('Position(s): ', a)
# else:
#     print('Not in list')
#print('Sum: ', sum(lt))
# a=0
# for i in lt:
#     a+=i
# print('Sum: ', a)
# ans=input("Enter list, elements seperated by ' ': ")
# a=ans.split(',')
# while ',' in a or '' in a:
#     ans=input("Enter list, elements seperated by ' ': ")
#     a=ans.split(',')
# for i in range(len(a)):
#         a[i]=int(a[i])
# print('Your string: ', a)
# # print('sum of list: ', sum(a))
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print('Even number: ', *b, sep=' ')

  