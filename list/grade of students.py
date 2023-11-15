"""
print the list of students who has atleast 1 a grade.
and other subjects with atleast b grade.
A-90+
B-(80-90)
fail- 50-
C - others
"""
studentlist=['sergio ramos','lionel messi','christiano ronaldo','Luka mordic','neymar']
csmarks=[90,64,96,98,23] # cs marks
mathmark=[90,80,96,48,73] # maths mark
engmark=[86,100,96,88,83] # english marks
students_with_goodgrades=[]
# find the students if they have atleast 1 A grade and others with atleast B grade. 
for mark in range(len(csmarks)):
    if((csmarks[mark] >= 90 or mathmark[mark] >= 90 or engmark[mark] >= 90) and (csmarks[mark]>=80 and mathmark[mark]>=80 and engmark[mark] >= 80)):
        students_with_goodgrades.append(studentlist[mark])
print("students with atlest 80 marks in all subjects and with atleast only one a grade:",students_with_goodgrades)

"""
OP
students with atlest 80 marks in all subjects and with atleast only one A grade: ['sergio ramos', 'christiano ronaldo']
"""