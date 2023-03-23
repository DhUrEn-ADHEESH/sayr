'''
3. Input is a number. Output is the number in English, Eg 134 output OneThreeFour

'''

# Define a list for the conversion
num_list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# Get the input number as a string
num_str = input("Enter a number: ")

# Convert each digit to its English representation and append to a list
num_english_list = [num_list[int(digit)] for digit in num_str]

# Join the list of English digits into a single string
num_english = " ".join(num_english_list)

print(num_english)
