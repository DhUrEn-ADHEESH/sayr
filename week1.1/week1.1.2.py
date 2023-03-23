'''
2. The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype
'''

print('what did you purchase?') #asking user for purchase
user_bought = input()

vadai_cost = 30
soda_cost = 20
sandwich_cost = 100

total_purchase = 0
if 'vadai' in user_bought :
    total_purchase += vadai_cost
elif 'soda' in user_bought:
     total_purchase += soda_cost
elif 'sandwich' in  user_bought:
     total_purchase += sandwich_cost

print('the total cost is',total_purchase)

amount_paid = int(input('the amount you are paying is:')) #getting the amount paid
change = amount_paid - total_purchase 

if change == 0:
     print('sorry no change')
else:
     print('the change amount is:',change)
     