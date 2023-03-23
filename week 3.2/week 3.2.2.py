'''
Python code to find all the characters that are in both input strings:

'''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common_chars = set(string1).intersection(set(string2))
print("Common characters: ",common_chars)
