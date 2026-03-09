account=int(input('enter account marks:'))
stat=int(input('enter stat marks:'))
eco=int(input('enter eco marks:'))
ocm=int(input('enter ocm marks:'))
english=int(input('enter english marks:'))
computer=int(input('enter computer marks:'))
total=account+stat+eco+ocm+english+computer
print(f'total mark are {total}')
per=total*100/600
print(per)
