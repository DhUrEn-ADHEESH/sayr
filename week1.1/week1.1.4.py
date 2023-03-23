
'''
5. Write a program to calculate the milege. Ask the user how many litres of petrol they have. 
Ask how many km they have to drive. Calcualte the milege. If the mileage is more than 30km per litre, tell 
the user they have to fill the tank again.
'''

#get the litres of petrol they have

amount_of_petrol = float(input('enter the litres of petrol you have: '))
distance = float(input('enter the distance to be travelled: '))

#to calculate mileage

car_mileage = distance / amount_of_petrol
print('the mileage is',car_mileage,'km per litre')

if car_mileage > 30:
    print('the mileage is more thn 30km per litre ,you have to refill')
else:
    print("no need to refill,keep going!!")
