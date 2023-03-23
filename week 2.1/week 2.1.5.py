'''
5. Same as above. Calculate his annual salary. He gets a bonus of Rs 5000 at the end of the year,
 if he sells 20 phones or more in a year.

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

yearly_salary = fixed_salary * 12 + comission #find yearly slary

print('the yearly salary is ',yearly_salary)

if no_of_phones >= 20:
    yearly_salary += 5000
    print('yearly salary after bonus is ',yearly_salary)
else:
    print('ther is no bonus')
