'''
1. Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'.
'''

name = (input('tell me your name: '))  #to get users name
print ('hello ',name)
year = int(input('tell me the year you are born: ')) #to get users year
present_year = 2023
age = present_year - year
print('you are',age,'years old')


