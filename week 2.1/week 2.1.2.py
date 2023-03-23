'''
2. Same as above. Do the grade avg for all the students in one class. Also, calculate the class average.

'''
no_of_students = int(input('no of students in a class is ' )) # get the number of students in a class
class_average = 0
for i in range (no_of_students):
    print('the student roll number is ',i+1) #print the roll number
#get the marks for five subjects
    m1 = int(input('science subject mark: '))
    m2 = int(input('social subject mark: '))
    m3 = int(input('math subject mark: '))
    m4 = int(input('english subject mark: '))
    m5 = int(input('language subject mark: '))
#average the marks of five subjects
    avg = (m1+m2+m3+m4+m5)/5

    print('the average mark of the student is ',avg) #print the average

    if avg >= 90 :
        print("The student has secured 'A' grade")
    elif avg >= 80 and avg < 90:
        print("the student has secured 'B' grade" )
    elif avg >= 70 and avg < 80 :
        print("the student has secured 'C' grade")
    else:
        print('the student did not pass the exam')

    class_average += avg 
    
print('the class average is ',class_average/no_of_students)#print the class average 