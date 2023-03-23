'''
. Get a city name from the user. Find out how many 'a' or 'e' is in the city name
'''

city = (input('Give me a city name:')) #get the city name
count = 0  #assign count value as 0
for char in city:
    if char == 'a':
        count += 1
    if char =='e':
        count += 1

print('The total count of a and e is',count)#print the output

