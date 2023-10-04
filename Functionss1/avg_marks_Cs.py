"""
Problem 1:
Write a program to calculate your avg marks in CS subject in the last 3 exams.
"""
 
# function to calculate average.
def calculate_avg_marks_CS(CS1,CS2,CS3):
    # the 3 marks are added and divided and rounded off to 2 decimal points.
    avg=format(((CS1+CS2+CS3)/3),".2f")
    return(avg)


computerScienceMrk1=float(input("enter your Computer Science mark in 1st exam:"))
computerScienceMrk2=float(input("enter your Computer Science mark in 2nd exam:"))
computerScienceMrk3=float(input("enter your Computer Science mark in 3rd exam:"))
# the defined function has been cakled and the arguments are passed.
average=calculate_avg_marks_CS(computerScienceMrk1,computerScienceMrk2,computerScienceMrk3)
print(f"your average is:{average}")


"""
OP:
enter your Computer Science mark in 1st exam:78
enter your Computer Science mark in 2nd exam:90
enter your Computer Science mark in 3rd exam:89
your average is:85.67
"""