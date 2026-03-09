print('Welcome to our SUNFLOWER CAFE ')
a=int(input('Please enter a number to order desserts [1-8]: '))
if a==1:
    print('Apple Pie    Price=$2')
elif a==2:
    print('Cherry Pie   Price=$3')
elif a==3:
    print('Ice Cream   Price=$3')
elif a==4:
    print('Seasonal Fruit   Price=$2')
elif a==5:
    print('Frozen Yogurt   Price=$3')
elif a==6:
    print('Rice Pudding   Price=$3')
elif a==7:
    print('Pancakes & Syrup   Price=$3')
elif a==8:
    print('Banana Split   Price=$5')
else:
    print('nothing is found')
    
b=int(input('Please enter a number to order desserts [1-4]: '))
match b:
    case 1:
        print('Apple Pie    Price=$2')
    case 2:
        print('Cherry Pie   Price=$3')
    case 3:
        print('Ice Cream   Price=$3')
    case 4:
        print('Seasonal Fruit   Price=$2')
    case _:
        print("Invalid number")
    