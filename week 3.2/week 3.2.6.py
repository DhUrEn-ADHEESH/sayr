'''
6. Input two strings. Output is both strings merged . Eg - input1 = ABCD, input 2 = 1234. Output = A1B2C3D4 


'''
#
a = 'abcd'
b = '1234'
#
c = ''.join(''.join(x) for x in zip(a,b))

print(c)

