'''
4. Input a string. 
    Print all the chars that are in Odd index - eg intput - abcd, output bd
    Print all the chars in the even index in reverse order - eg input abcd output ca
'''
# get a string as input
strName = input('enter a string: ') 
print('the characters in odd index are ',strName[1::2])
reverseStr = strName[::2]
# use reversed function to reverse the sliced string
string = "".join(reversed(reverseStr))
print('the characters in the even index in reversed order are ',string)