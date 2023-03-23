'''
Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
    until the length is equal. 
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cataa, arrow (length is equal by adding a)

'''
name1 = input('Enter the first name: ')
name2 = input('Enter the second name: ')

if len(name1) != len(name2):
    if len(name1) < len(name2):
        name1 += 'a' * (len(name2) - len(name1))
    else:
        name2 += 'a' * (len(name1) - len(name2))

print(name1, name2)