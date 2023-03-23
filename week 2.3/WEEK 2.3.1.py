'''
1.  You are going to a shop to buy candies and chochlates. 100g of candy is Rs50. 100g of chochlate is 
 Rs150. You buy 100g of candy first.
Then if you have more money left, you buy 100g of chochlate. You check again and buy  candies and then buy chochlates
You buy as much candy or choc0late as you can with the money you have.
Input is your budget, output is the amount of candy and/or chochlate you bought.
'''

budget = int(input("Enter your budget: "))  #take budget from user

candy_price = 50  #price of 100g of candy
chocolate_price = 150  #price of 100g of chocolate

candy = 0  #initialize amount of candy bought
chocolate = 0  #initialize amount of chocolate bought

choice_of_user = input('What do you want to buy? (candy/chocolate) ')

# buy candy or chocolate based on user's choice and available budget
if budget >= candy_price and choice_of_user == 'candy':
    candy += 1
    budget -= candy_price
    print('You bought candy. The remaining budget is', budget)
elif budget >= chocolate_price and choice_of_user == 'chocolate':
    chocolate += 1
    budget -= chocolate_price
    print('You bought chocolate. The remaining budget is', budget)
else:
    print('Sorry, not enough budget to buy', choice_of_user)
    exit()

# buy more candy or chocolate with the remaining budget (if any)
user_choice = input('Do you want to buy again? (yes/no) ')
while user_choice == 'yes' and (budget >= candy_price or budget >= chocolate_price):
    second_choice = input('What do you want to buy? (candy/chocolate/enough) ')
    if second_choice == 'candy' and budget >= candy_price:
        candy += 1
        budget -= candy_price
        print('You bought candy. The remaining budget is', budget)
    elif second_choice == 'chocolate' and budget >= chocolate_price:
        chocolate += 1
        budget -= chocolate_price
        print('You bought chocolate. The remaining budget is', budget)
    elif second_choice == 'enough':
        print('Thank you! Come again.')
        break
    else:
        print('Sorry, not enough budget to buy', second_choice)
    user_choice = input('Do you want to buy again? (yes/no) ')

# print the amount of candy and chocolate bought
print("Amount of candy bought:", candy*100, "grams")
print("Amount of chocolate bought:", chocolate*100, "grams")
print('THANKS FOR YOUR VISIT!COME AGAIN')

