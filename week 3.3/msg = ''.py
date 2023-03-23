msg=''
index=0
message="IloveIndia"
pattern="*** **** ** ***************"


for char in pattern:
    if char == '*':
        if index < len(message):
            msg += message[index]
            index += 1
        else:
            # Reset the index to 0 if the end of the message is reached
            index = 0
       
    else:
        msg += char



print("message return pattern:", msg)
