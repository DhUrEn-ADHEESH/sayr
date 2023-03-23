'''
You are going to a movie with your friends. Each of you buy a ticket and buy a snack or a drink.
Each ticket is Rs200. Popcorn small is Rs 50, medium is Rs 100 and Large is Rs 150. Coke is Rs 80.
What is the total cost for each person and total cost for all of your friends. 
 

2.1. Same as above. Find which friend spent the most money. 

2.2. Same as above. Find out how many friends liked and how many friends disliked the movie. 

2.3  Same as above problem. Find the average of cost per person. The theatre makes 20% profit on the 
avg from each person going to the movie. What is the profit of the theatre for this one show you attended?
Hint - to find out the profit, you need to get one additional input from your user. 
'''

tktPrice = 200
smallPop = 50
medPop = 100
largePop = 150
coke = 80
noOfFrnds = int(input('No of friends joining: '))
totalAmo = 0
sChoice = 0
noChoice = 0
costPerPerson = []

for frnd in range(noOfFrnds):
    print('Friend no is', frnd+1)
    choice = input('Do you want a snack or a drink? ')
    if choice == 'snack':
        choiceOfPop = input('Do you want a small, medium, or large popcorn? ')
        if choiceOfPop == 'small':
            print('Here is your small popcorn.')
            amtSpnt = smallPop + tktPrice
            print('Total amount you have spent is', amtSpnt)
            totalAmo += amtSpnt
        elif choiceOfPop == 'medium':
            print('Here is your medium popcorn.')
            amtSpnt = medPop + tktPrice
            print('Total amount you have spent is', amtSpnt)
            totalAmo += amtSpnt
        elif choiceOfPop == 'large':
            print('Here is your large popcorn.')
            amtSpnt = largePop + tktPrice
            print('Total amount you have spent is', amtSpnt)
            totalAmo += amtSpnt
        else:
            print('Invalid choice.')
            amtSpnt = 0
    elif choice == 'drink':
        print('Here is your coke.')
        amtSpnt = coke + tktPrice
        print('Total amount you have spent is', amtSpnt)
        totalAmo += amtSpnt
    else:
        print('Invalid choice.')
        amtSpnt = 0

    costPerPerson.append(amtSpnt)

print(costPerPerson)

maxSpending = costPerPerson[0]
maxFriend = 1
for i in range(1, noOfFrnds):
    if costPerPerson[i] > maxSpending:
        maxSpending = costPerPerson[i]
        maxFriend += i

print('The total amount spent is', totalAmo)
print('The friend who spent the most is friend', maxFriend, 'who spent Rs', maxSpending)

for frnd in range(noOfFrnds):
    print('Friend no is', frnd+1)
    movieLiked = input('Did you like the movie? (yes or no) ')

    if movieLiked == 'yes':
        sChoice += 1
    elif movieLiked == 'no':
        noChoice += 1

print('No of people who liked the movie:', sChoice)
print('No of people who disliked the movie:', noChoice)

avgCostPerCust = totalAmo / noOfFrnds
print('The average cost per customer is', avgCostPerCust)
theatre_profit_per_person = 0.2 * avgCostPerCust
theatre_profit = theatre_profit_per_person * noOfFrnds
print('theatre profit is ',theatre_profit)



      




        


     
