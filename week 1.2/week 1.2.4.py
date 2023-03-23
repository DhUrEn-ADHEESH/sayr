'''
9.Start with the above. The total cost is split equally by bride and groom.
 Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
 If loan, how much?
'''

#get no of guests
no_of_guests = int(input('total number of customers is '))

lunch_per_person = 200 #initialize the values 
breakfast_per_person = 100
hall_cost_per_person = 200

breakfast_cost = breakfast_per_person * no_of_guests #calculate the cost of breakfast,lunch and hall
print('total cost of breakfast is:',breakfast_cost)
lunch_cost = lunch_per_person * no_of_guests
print('total cost of lunch is:',lunch_cost)
hall_cost = hall_cost_per_person * no_of_guests
print('total cost of hall is:',hall_cost)

decoration_cost = hall_cost * 0.5 #calculate decoration cost
print('decoration cost is :',decoration_cost)

parking_cost = hall_cost *0.1 #calculate parking cost
print('parking cost is :',parking_cost)
 
total_cost_of_marriage = breakfast_cost + lunch_cost+ hall_cost+decoration_cost+parking_cost #find the total cost
print('the total cost of marriage is',total_cost_of_marriage)


splitted_amount = total_cost_of_marriage / 2   #find the amount to be splitted between the groom and the bride
print('the amount to be splitted between the groom and the bride is',splitted_amount)

if splitted_amount > 50000:
    loan_to_be_taken = splitted_amount - 50000 #find amount of loan  to be taken
    print('loan has to be taken')
    print('the amount is :',loan_to_be_taken)
else:
    print('No need to take loan')