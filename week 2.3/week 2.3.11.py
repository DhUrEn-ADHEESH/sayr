
budget = int(input("Enter your budget: "))  #take budget from user

candy_price = 50  #price of 100g of candy
chocolate_price = 150  #price of 100g of chocolate

candy = 0  #initialize amount of candy bought
chocolate = 0  #initialize amount of chocolate bought
totalCost = 0

while budget >= 50:
  print('100 gms of candy was bought ')
  budget -= candy_price
  totalCost += candy_price
  if budget >= 150:
    budget -= chocolate_price
    print('100 gms of chocolate was bought ')
    totalCost += chocolate_price
else:
  print('Budget is less than 50')

print(totalCost)















# while budget >= 50:
#     choice_of_user = input('What do you want to buy? (candy) ')
#     if budget >= candy_price and choice_of_user == 'candy':
#         candy += 1
#         budget -= candy_price
#         totalCost+= candy_price
#         print('You bought candy. The remaining budget is', budget)
#     elif budget >= chocolate_price and choice_of_user == 'chocolate':
#        chocolate += 1
#        budget -= chocolate_price
#        totalCost += chocolate_price
#        print('You bought chocolate. The remaining budget is', budget)
# else:
#     print('budget is less than 50')


# print(totalCost)
