#BAI_2
month=int(input('enter month:'))
while month>12 or month==0:
        print('sai roi')
        month=int(input('enter month:'))
if month in range(1,4):
        print('Xuan')
elif month in range(4,8):
        print('Ha')
elif month in range(8,11):
        print('Thu')
else:
        print('Dong')