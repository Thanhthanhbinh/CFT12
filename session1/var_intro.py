print('type number:')
num = eval(input('number here:'))
yn = input('more number? ')
if yn == 'yes' or yn == 'Yes':
    # triangle
    num2 = eval(input('number here:'))
    area = (num*num2)/2
    print('this is a triangle', ",the area of said triangle:", area)
else:
    # circle
    area = (num**2)*3.14
    print('this is a circle', ",the area of said circle:", area)
print("('_') - End.")
    