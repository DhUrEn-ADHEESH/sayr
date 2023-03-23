'''
. Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"

     Note how you replace each * in the pattern with the letter in the message, the space in the message doesn't
     matter, but the space(s) in the pattern matters.

'''
# Get the input message and pattern
message = 'iloveindia'
pattern = '*** ***** **** *** *************** ***'

# Initialize the output string and index variables
output = ""
message_index = 0
pattern_index = 0

while pattern_index < len(pattern):
    if pattern[pattern_index] == " ":
        output += " "
        pattern_index += 1
    elif pattern[pattern_index] == "*":
        if message_index < len(message):
            output += message[message_index]
            message_index += 1
            pattern_index += 1
        else:
            message_index = 0
   

# Print the output string
print(output)


