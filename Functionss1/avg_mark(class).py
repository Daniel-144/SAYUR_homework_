"""
Problem 2:
Write a program to calculate avg marks of your class, in CS subject in the last 3 exams.
"""
# function to collect the name.
def collecting_names(rollno):
    name=input(f"enter the name of the student(ROLL.No:{rollno+1}):")
    return(name)

# function to collect the marks.
def collecting_marks(rollno):
    cS1=int(input(f"enter the mark of student {rollno+1} in CS 1st exam:"))
    cS2=int(input(f"enter the mark of student {rollno+1} in CS 2nd exam:"))
    cS3=int(input(f"enter the mark of student {rollno+1} in CS 3rd exam:"))
    print()
    return((cS1,cS2,cS3))

# function to calculate the average of the students.
def calculating_average(rollno,csMarks):
    average=0
    for i in range(len(csMarks)):
        average+=csMarks[i]
    average=format(average/len(csMarks),".2f")
    return(average)


# initializing the lists.
namelist=[]
csMarkList=[]
average=[]
above_75per=[]
NoStudents=int(input("enter the total number of students: "))
# loop to store the names,marks and average in a list.
for i in range(NoStudents):
    namelist.append(collecting_names(i))
    csMarkList.append(collecting_marks(i))
    average.append(calculating_average(i,csMarkList[i]))
print("'the average of the students.'")
# loop to print the average of the students.
for student in range(NoStudents):
    print(f"the average of the studen{student+1}-{namelist[student]} is {average[student]}")



"""
Op:
enter the total number of students: 3
enter the name of the student(ROLL.No:1):vegeta
enter the mark of student 1 in CS 1st exam:90
enter the mark of student 1 in CS 2nd exam:90
enter the mark of student 1 in CS 3rd exam:90

enter the name of the student(ROLL.No:2):krilin
enter the mark of student 2 in CS 1st exam:20
enter the mark of student 2 in CS 2nd exam:89
enter the mark of student 2 in CS 3rd exam:100

enter the name of the student(ROLL.No:3):asta
enter the mark of student 3 in CS 1st exam:80
enter the mark of student 3 in CS 2nd exam:79
enter the mark of student 3 in CS 3rd exam:81

'the average of the students.'
the average of the studen1-vegeta is 90.00
the average of the studen2-krilin is 69.67
the average of the studen3-asta is 80.00
"""
