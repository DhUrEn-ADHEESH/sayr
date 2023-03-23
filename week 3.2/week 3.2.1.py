'''
In the input, find the first A and last A, print all the letters between these two A.

'''

input_str = input("Enter a string: ")
first_a = input_str.find("A")
last_a = input_str.rfind("a")

if first_a == -1 or last_a == -1:
    print("A not found in the string")
else:
    print(input_str[first_a+1:last_a])
