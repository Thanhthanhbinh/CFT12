#BAI1_02Mrch
# first=input('Enter first name: ')
# last=input('Enter last name: ')
# print('Your name: ', first,last)
# first=first.upper()
# last=last.upper()
# print('Your name: ', first,last)

#BAI2_02Mrch
# import re
#num=int(input('Enter number: '))
# #loc khong hoan toan so va khong co cham
# while num.isdigit()==False and num.rfind('.')!=1 :
#     num=input('Enter number: ')
# if num.isdigit():
#     num=int(num)
#     num=num**2
#     print('Your number: ', num)
# elif num.index(".")==1:
#     num=float(num)
#     num=num**2
#     print('Your number: ', round(num,2))
# num=int(num)
# num=num**2
# print('Your number:', num)
    
#BAI3_02Mrch/09Mrch
# from turtle import *
# rad=int(input('Enter number: '))
# shape('turtle')
# color('blue')
# circle(rad)
#mainloop()

#BAI4_09Mrch
# b=""
# num=int(input('Enter number: '))
# while num<0:
#     num=int(input('Enter number: '))
# for i in range(-num+1,0,2):
#     a=str(-i)
#     b+=a
#     b+=' '
# print(b)

#BAI5_09Mrch
# from turtle import *
# num=int(input('Enter number: '))
# shape('triangle')
# color('blue')
# for i in range(num):
#     forward(100)
#     left(360/num)
# mainloop()

#BAI6_09Mrch
# import re
# passW=input('Enter username: ')
# userN=input('Enter password: ')
# while len(userN)<8:
#     userN=input('Enter password: ')
# while userN.isdigit() or userN.isalpha():
#         userN=input('Enter password: ')
# # while len(re.findall(r'\d+',userN))==len(userN) :
# #     userN=input('Enter password: ')
# reUserN= input("Enter password again: ")
# while reUserN!=userN:
#     reUserN=input('Enter password again: ')
# email=input('Email please: ')
# while re.match('[^@]+@[^@]+\.[^@]+',email)==None:
#     email=input('Email please: ')

#BAI5_09Mrch
# num=int(input('Enter a number: '))
# if num<12:
#     if num not in [2]:
#         if num%2==0 and num!=8 :
#             print(30)
#         else:
#             print(31)
#     else:
#         if num==2:
#             print(28)

#BAI6_09Mrch
import random
from turtle import*
d=0
while True:
    a=random.randint(0,10)
    b=random.randint(0,10)
    c=random.randint(0,10)
    print(str(a),'+',str(b),'=',str(c))
    penup()
    write(str(a) +' + '+ str(b) +' = '+str(c), True, align="center")
    #num=input('True or False: ')
    num=textinput("Answer", "True or False:")
    if num not in ['True','False','true','false']:
        break
    if a+b==c and num in['false','False']:
        break
    elif a+b!=c and num in['true','True']:
        break
    d+=1
    clear()
print('Your diem:', d)
write('   '+str(d), True, align="left")
mainloop()
