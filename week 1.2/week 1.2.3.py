'''
Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost.
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



