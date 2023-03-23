'''
1. Get the marks for 10th stundet's math paper from 5 different exams. Calculate the average values. 
Calcualte if the student got A grade (avg > 90) or B grade (avg > 80) or C grade (avg > 70) or fail.
'''

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