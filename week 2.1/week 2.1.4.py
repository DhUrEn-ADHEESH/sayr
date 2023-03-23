'''
4. Calcualte the salary of the phone salesman for a month. His monthly salary is Rs10000. If he sells a phone for 
Rs 15000 or more, he gets Rs1000 commission per phone. If sells a phone for Rs40000 or more, he gets Rs2000 per phone in commision.
He can earn a commision of Rs 10000 a month at the most.


'''

fixed_salary = 10000 #initializing the values to the variable
comission = 0

no_of_phones = int(input('enter the no of phones sold '))#enter the no of phones soled
for i in range(no_of_phones):
    phone_cost = int(input('enter the price of phones:'))#enter the price of phones sold
    if phone_cost >= 15000 and phone_cost < 40000:
        comission += 1000
    elif phone_cost >= 40000:
       comission += 2000
    
    if comission >= 10000:
        comission = 10000
        break
        

total_salary = comission + fixed_salary
print('the total salary is',total_salary)#print the total salary
      