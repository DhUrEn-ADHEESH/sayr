'''
7.Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget. 
7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
7.2 Same as above, but add 3% of the budget for petrol expenses. 
'''

user_budget = int(input('the amount user spends:')) #get the budget
petrol_expenses = 0.03 * user_budget
user_budget+=petrol_expenses      #adding petrol expenses
user_choice = input('select the city where you want to buy: ')#get the city
chennai_onion_price = 30   #get the prices
trichy_onion_price = 27
madurai_onion_price = 34

chennai_onion_quantity = round(user_budget / chennai_onion_price,2)  #calculate the prices
trichy_onion_quantity = round(user_budget / trichy_onion_price,2)
madurai_onion_quantity = round(user_budget / madurai_onion_price,2)

if user_choice == 'chennai' :
    print('The quantity is',chennai_onion_quantity,'kg')
elif  user_choice == 'trichy':
    print('The quantity is',trichy_onion_quantity,'kg')
elif user_choice == 'madurai':
    print('The quantity is',madurai_onion_quantity,'kg')
else:
    print('enter chennai,madurai or trichy')


'''
onion_price = 20  #get  onion price
tomato_price = 10.5 #get tomato price

onion_quantity = user_budget / onion_price
tomato_quantity = round(user_budget / tomato_price,2)   
#printing the output
print('the quantity of onion that can be bought is ',onion_quantity,'kg')
print('the quantity of tomato that can be bought is ',tomato_quantity,'kg')
'''
