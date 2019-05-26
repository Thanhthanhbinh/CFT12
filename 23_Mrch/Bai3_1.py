lt_na=['ST','BD','BTL','CG','DD','HTB']
lt_pe=[150300,247100,333300,266800,420900,318000]
lt_ar=[11743,9.224,43.35,12.04,9.96,10.09]
lt_md=[]
maxx=0
a=0
for i in range(len(lt_pe)):
    if lt_pe[i]>maxx:
        maxx=lt_pe[i]
        a=i
print('District with largest population: ', lt_na[a])
maxx=lt_pe[0]
a=0
for i in range(len(lt_pe)):
    if lt_pe[i]<maxx:
        maxx=lt_pe[i]
        a=i
        print(1)
print('District with smallest population: ', lt_na[a])
for i in range(len(lt_ar)-1):
    a=round(lt_pe[i]/lt_ar[i])
    lt_md.append(a)
print(lt_md)
a=len(lt_na)/sum(lt_md)
print('Aum md: ', a)