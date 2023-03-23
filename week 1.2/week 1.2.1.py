'''
6. Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college.
(hint - use if/elif)

'''

user_name = str(input('tell your name: ')) #get users name
print('hello', user_name)
user_year = int(input('tell me the year you were born: ')) #get users yer they were born
present_year = 2023
user_age = present_year - user_year
print('age is',user_age)

if user_age <= 3:
    print('There is time to go to school')
elif user_age > 3 and user_age < 6:
    print(user_name,'is going to preschool')
elif user_age > 6 and user_age <12 :
    print(user_name,'is going to elementary')
elif user_age > 12 and user_age < 16:
    print(user_name,'is going to middle school')
elif user_age > 16 and user_age < 18 :
    print(user_name,'is going to highschool')
else:
    print(user_name,'is going to college') 



