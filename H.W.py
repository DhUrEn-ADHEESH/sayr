'''
1. In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.
  2. Extension of Cafe
    2.1Replenish supply for every 5 customers  and at the end of the day

    2.2 Calculate replenish supply at the starting of the day for hot items, every 5 customers for all items and only cold items  at the every end of the day.
'''

input_str = input("Enter a string: ")


def find_bet(first_char, second_char, input_str):
    first_word = input_str.find(first_char)
    last_word = input_str.rfind(second_char)
    if first_word ==  last_word  :
        return None
    else:
        return input_str[first_word+1:last_word]

def find_word(input_str):
    search = find_bet("A", "A", input_str)
    if search is None:
        search = find_bet("B", "B", input_str)
    if search is None:
        search = find_bet("C", "C", input_str)
    if search is None:
        print("No characters found in the input string.")
    else:
        print(search)


find_word(input_str)





