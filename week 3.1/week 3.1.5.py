'''
 Same program as above. Instead of adding 'a' at the end of the short name, add the last letter.
    Eg - input - cat, arrow. (legnth is not equal) 
    Output - cattt, arrow (length is equal by adding the last letter of Cat)

'''
name1 = input('Enter the first name: ')
name2 = input('Enter the second name: ')

if len(name1) != len(name2):
    if len(name1) < len(name2):
        name1 += name1[-1] * (len(name2) - len(name1))
    else:
        name2 += name2[-1] * (len(name1) - len(name2))

print(name1, name2)