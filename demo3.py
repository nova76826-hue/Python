unit=int(input('Enter the unit which you has used :'))
if unit<=50:
    bill=unit*3.05
    
elif unit<=100:
    bill=(50*3.05)+ (unit-50)*3.50
    
    
elif unit<=200:
    bill=(50*3.05)+ (50*3.50)+(unit-100)*4.15
    
   

elif unit<=300:
    bill=(50*3.05)+(50*3.50)+(100*4.15)+(unit-200)*4.40
    
   

else:
    bill=(50*3.05)+(50*3.50)+(100*4.15)+(100*4.40)+(unit-300)*5.50
    

print('bill=',bill)