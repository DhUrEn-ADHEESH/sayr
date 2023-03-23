'''
4. Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
Find the answer and print. '''


#asking the user for three numbers
x = int(input('the first number is:'))
y = int(input('the second number is:'))
z = int(input('the third number is:'))

#asking the user if they want the max or min

user_choice=input(('do you want to find the maximum or minimum ??  '))

if 'maximum' in user_choice:  #printing the max or min number
    print('the maximum number is',max(x,y,z))
else:
    print('the minimum number is',min(x,y,z))

