# The student has 100 marks in any one subject, Grade is A.
#if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D
#Code
mark1 = int(input('enter the mark in subject 1'))
mark2 = int(input('enter the mark in subject 2'))
mark3 = int(input('enter the mark in subject 3'))
if (mark1<0 or mark1>100) (mark3<0 or mark3>100) (mark2<0 or mark2>100):
    print('invalid mark cannot be negative')
else:
 if(mark1 == 100 or mark2 == 100 or mark3 == 100) :
    print ('your grade is A')
 elif (mark1 >=90  or  mark2>90  or mark3>90):
    print ("your Grade B")
 elif (mark1 >=60 or mark2>=60  or mark3>=60 and mark3<90):
    print('your grade is C')
 elif mark1 <=50 and mark2 <=50 and mark3 <=50 :
    print('your grade is F')
 else:
    print('your grade is D')