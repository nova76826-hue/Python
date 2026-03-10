total = 0
while True:

    a = int(input("Select Category (1=Soups, 2=Salad, 3=Chinese, 4=Noodles, 0=Finish): "))

    if a == 0:
        break
    
    if a==1:
        print('SOUPS')
        b=int(input('soups[1-16] : '))
        if b==1:
            print('TOMATO BASIL = 199')
            total += 199
        elif b==2:
            print('MANCHOW = 210')
            total += 210
        elif b==3:
            print('HOT GARLIC = 220')
            total += 220
        elif b==4:
            print('MINESTRONE = 220')
            total += 220
        elif b==5:
            print('LEMON CORIANDER = 220')
            total += 220
        elif b==6:
            print('WILD MUSHROOM = 230')
            total += 230
        elif b==7:
            print('CHILLY BEAN SOUP = 230')
            total += 230
        elif b==8:
            print('ROASTED ALMOND BROCCOLI = 250')
            total += 250
        elif b==9:
            print('TOM YUM SOUP = 250')
            total += 250
        elif b==10:
            print('KHOW SUEY SOUP = 330')
            total += 330
        elif b==11:
            print('BROCCOLI & CHEDDAR SOUP = 389')
            total += 389
        elif b==12:
            print('VEG DUMPING SOUP = 230')
            total += 230
        elif b==13:
            print('HOT POT SOUP = 250')
            total += 250
        elif b==14:
            print('FILIPINO SOUP = 260')
            total += 260
        elif b==15:
            print('TOM KHA SOUP = 220')
            total += 220
        elif b==16:
            print('SWEETCORN SOUP = 199')
            total += 199

    elif a==2:
        print('SALAD')
        b=int(input('salad[1-6] : '))
        if b==1:
            print('CEASAR SALAD = 290')
            total += 290
        elif b==2:
            print('FATTOUSH SALAD = 280')
            total += 280
        elif b==3:
            print('ANTIPASTI = 280')
            total += 280
        elif b==4:
            print('GREEN SALAD = 130')
            130
        elif b==5:
            print('SOM TOM SALAD = 290')
            total += 290
        elif b==6:
            print('GREEK SALAD = 310')
            total += 310

    elif a==3:
        print('CHINESE')
        b=int(input('salad[1-11] : '))
        if b==1:
            print('VEG. MANCHURIAN = 290')
            total += 290
        elif b==2:
            print('VEG. CRISPY ( GREEN/RED ) = 310')
            total += 310
        elif b==3:
            print('CHILLI BABY CORN = 335')
            total += 335
        elif b==4:
            print('JUNGLI PANEER = 360')
            total += 360
        elif b==5:
            print('PANEER RED COOK / PANEER CHILLI = 360')
            total += 360
        elif b==6:
            print('AMERICAN CORN SALT & PEPPER = 310')
            total += 310
        elif b==7:
            print('BUTTER GARLIC VEGETABLE = 470')
            total += 470
        elif b==8:
            print('SAIWOO PANEER = 390')
            total += 390
        elif b==9:
            print('THREAD PANEER(MUST TRY) = 470')
            total += 470
        elif b==10:
            print('SPINACH COTTAGE CHEESE BALL IN SWEET = 399')
            total += 399
        elif b==11:
            print('SHANGHAI SPRING ROLL = 280')
            total += 280

    elif a==4:
        print('NOODLES')
        b=int(input('salad[1-6] : '))
        if b==1:
            print('VEG. HAKKA NOODLES = 280')
            total += 280
        elif b==2:
            print('SCHEZWAN NOODLES = 310')
            total += 310
        elif b==3:
            print('SINGAPORE NOODLES = 345')
            total += 345
        elif b==4:
            print('AMERICAN CHOP SUEY = 320')
            total += 320
        elif b==5:
            print('PAD THAI NOODLES = 330')
            total += 330
        elif b==6:
            print('CHILLY GARLIC NOODLES = 330')
            total += 330
print("Total Bill =", total)