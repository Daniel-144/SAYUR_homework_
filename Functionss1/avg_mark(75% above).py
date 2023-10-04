"""
Problem 3:
Write a program to calculate avg marks for each student and no of students whose avg is above 75%
in CS subject in the last 3 exams.
"""

# function to get the names from the user.
def collecting_names(rollno):
    name=input(f"enter the name of the student(ROLL.No:{rollno+1}):")
    return(name)

# function to get the marks from the user.
def collecting_marks(rollno):
    cS1=int(input(f"enter the mark of student {rollno+1} in CS 1st exam:"))
    cS2=int(input(f"enter the mark of student {rollno+1} in CS 2nd exam:"))
    cS3=int(input(f"enter the mark of student {rollno+1} in CS 3rd exam:"))
    # the input marks are returned as a tuple.
    return((cS1,cS2,cS3))

# function to calculate the average.
def calculating_average(rollno,csMarks):
    average=0
    for i in range(len(csMarks)):
        average+=csMarks[i]
    average=format(average/len(csMarks),".2f")
    return(average)

# initializing the lists to store the data
namelist=[]
csMarkList=[]
average=[]
above_75per=[]
NoStudents=int(input("enter the total number of students: "))
# loop to collect, calculate and filter the persons with above 75%.
for i in range(NoStudents):
    # the function collecting names is called and the name returened from the function is appended in the list.
    namelist.append(collecting_names(i))
    # the function collecting marks is called and the mark returned from the function is appended in the list.
    csMarkList.append(collecting_marks(i))
    # the function calculating_average is called and the average returned from the function is appended in list.
    average.append(calculating_average(i,csMarkList[i]))
    # to filter the students with an average of above 75%
    if (float(average[i])>75):
        above_75per.append(namelist[i])

print(f"the students with average greater than 75%: {above_75per}")

