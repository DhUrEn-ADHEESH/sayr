'''
2. We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2.
'''

#get the marks for 5 different subjects from students
subject_1 = int(input('enter the marks for subject 1 : '))
subject_2 = int(input('enter the marks for subject 2 : '))
subject_3 = int(input('enter the marks for subject 3 : '))
subject_4 = int(input('enter the marks for subject 4 : '))
subject_5 = int(input('enter the marks for subject 5 : '))
#find the average
avg_mark = (subject_1 + subject_2 + subject_3 + subject_4 + subject_5)/5
print("the average mark is : ",avg_mark)

if avg_mark > 88 and avg_mark <= 92:
    print("the student is eligible to get admission in college 2 ")
elif avg_mark > 92 and avg_mark <=96:
        print("the student is eligible to get admission in college 1 and college 2")
elif avg_mark > 96:
          print("the student is eligible to get admission in college 2,college 1 and college 3")
else:
       print('sry no college is available')

