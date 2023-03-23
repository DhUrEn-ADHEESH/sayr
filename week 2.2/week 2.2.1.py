'''
1.Get the marks for 3 subjects from the students.

 If the mark is greater than 75 in any two subjects, then print Pass and also print the subject where the marks in > 75
 If the marks is greater than 60 in all three subjects, then print pass.
  If the student scored in 100 in any one subject, it is pass.  Print which subject the student scored 100.
 if the above conditions  not met, print fail.
'''

#get the marks for 3 subjects from the student
subject1_mark = int(input("enter marks for subject 1: "))
subject2_mark = int(input("enter marks for subject 2: "))
subject3_mark = int(input("enter marks for subject 3: "))
#check if the student passes
if (subject1_mark  == 100) or (subject2_mark == 100) or (subject3_mark == 100):
    if subject1_mark == 100:
        print("Pass! subject 1 score is 100.")
    elif subject2_mark == 100:
        print("Pass! subject 2 score is 100.")
    else:
        print("Pass! subject 3 score is 100.")
elif  (subject1_mark > 75 and subject2_mark > 75) or (subject2_mark > 75 and subject3_mark > 75) or (subject3_mark > 75 and subject1_mark > 75) or (subject1_mark > 75 and subject2_mark > 75 and subject3_mark > 75):
    if subject1_mark > 75 and subject2_mark > 75 and subject3_mark > 75:
        print("Pass! subject 1,subject 2 and subject 3 score is > 75 ")
    elif subject1_mark > 75 and subject2_mark > 75:
        print("Pass! subject 1 and subject 2 score is > 75.")
    elif subject2_mark > 75 and subject3_mark > 75:
        print("Pass! subject 2 and subject 3 score is > 75.")
    elif subject3_mark > 75 and subject1_mark > 75:
        print("Pass! subject 3 and subject 1 score is > 75.")
elif subject1_mark > 60 and subject2_mark > 60 and subject3_mark > 60:
    print("Pass! student scored > 60 in all three subjects.")
else:
    print("Fail! student did not meet passing criteria.")
