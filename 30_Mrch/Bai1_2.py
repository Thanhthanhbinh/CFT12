dictt={'name':'Tony','age':23,'nationality':'American','status':'''ldflskfjlsflsfjlsdjflkdsf
fksjdflskjfkljdfladsjfkljaklfjalkfjff fjljflsflfjl '''}
while True:
    ans=input('Enter:')
    b=ans.lower()
    while b not in dictt:
        ans=input('Enter again please: ')
        b=ans.lower()
        if ans=='e':
            break
    print(dictt[b])