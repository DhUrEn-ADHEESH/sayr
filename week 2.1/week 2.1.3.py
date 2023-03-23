'''
3. Same as above. Do it for all the 10th classes in a school. Calcualte the school average.
'''
no_of_section = int(input('no of sections is ')) #get the no of sections
no_of_students = int(input('no of students in a class is ' )) # get the number of students in a class

for s in range(no_of_section):
    print('the section is ',s+1)
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
        
    total_avg = class_average/no_of_students
    print('the class average of section ',s+1,'is',total_avg)#print the class average 
    
school_avg = total_avg / no_of_section#to print the school avg
print('the school average is ',school_avg)