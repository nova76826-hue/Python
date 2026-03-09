'''x=['gmiu',123,'have a nice day']
print(x)

y=['gmiu','bhavanagar','application','of','bscit']
print(y[3])

a='gmiu'
b=a.upper()
print(b)

a='gmiu collage'
c=a.title()
print(c)

q='kjvgjlg'
print(q.isupper())

e='wordew'
print(e.count('w'))

t='abcdefghijklmnopqrst'
import sys
print(sys.version)'''
a=int(input('enter the value of a :'))
if a>= 0:
    print('a is positive')
else:
    print('a is negative')
    
day=366
if day==366:
    print('current year is leap year')
else:
    print('it is not leap year')
    
q=int(input('enter the value of q :'))
w=int(input('enter the value of w :'))
if q<w:
    print('q is greater')
else:
    print('w is greater')

age=int(input('enter the value of age :'))
if age>=18:
    print('you are eligible for vote')
else:
    print('you can not vote')
    
i=int(input('enter the value of i :'))
o=int(input('enter the value of o :'))
p=int(input('enter the value of p :'))
if i>o:
    if i>p:
        print('i is greater')
    else:
        print('p is greater')
elif o>p:
    print('o is greater')
else:
    print('p is greater')
    
    
j=int(input('enter the value of j :'))
if j%5==0:
    print('divid by 5')
else:
    print('can not divide')
    
sum=('a,e,o,u')
um=('a,e,i,o,u')
if sum <= um:
    print('sum is vow3els')
else:
    print('sum is not vowelsw')
    
y=int(input('enter the value of y :'))
if y%2==0:
    print('give num is even')
else:
    print('given num is odd')
    
per=int(input('enter the your per :'))
if per>=90:
    print('you have A+ grade')
elif per>=80:
    print('you have A grade')
elif per>=70:
    print('you have B+ grade')
elif per>=60:
    print('you have B grade')    
elif per>=50:
    print('you have C grade')
elif per>=40:
    print('you have D grade')
elif per>=35:
    print('you have PASSing grade')
else:
    print('you are fail!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
