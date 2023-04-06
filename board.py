'''
 Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game.

'''
def split_number(num):
    digits = []
    for digit_str in num:
        digit = int(digit_str)
        digits.append(digit)
    return digits

user1_Score = 0
user2_Score = 0

def userpos(list1, list2):
    global user1_Score, user2_Score
    if (abs(list1[0] - list2[0]) == 0) and (abs(list1[1] - list2[1]) == 0):
        user2_Score += 1
        print("User2's Score: ", user2_Score)
    elif (abs(list1[0] - list2[0]) <= 1) and (abs(list1[1] - list2[1]) <= 1):
        user1_Score += 1
        print("User1's Score: ", user1_Score)

while user1_Score < 5 and user2_Score < 5:
    user1 = input('Enter the row and column for User1: ')
    user1_score = split_number(user1)

    user2 = input('Enter the row and column for User2: ')
    user2_score = split_number(user2)

    userpos(user1_score, user2_score)

if user1_Score == 5:
        print("User 1 wins!")
        
elif user2_Score == 5:
        print("User 2 wins!")
        

        
        






   
    


'''
if (abs(list1[0] - list2[0])= 1) and (abs(list1[1] -list2[1]) = 1):
'''

