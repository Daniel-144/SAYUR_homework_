######## Problem  1 ###############
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc
number_of_students=int(input("Enter number of students :"))
marks_count=int(input("Enter number of subjects :"))
#loop for collecting the details of the student
for student in range (number_of_students):
    name=input(f"Enter name of student {student+1} :")
    for mark in range(marks_count):
        inputMark = float (input(f"Enter mark{mark+1} of Student {name} :")) #use formatted string 
        print(f"Mark {mark+1} for Student {name} is {inputMark}")     
    print("")

"""
OP
Enter number of students :3
Enter number of subjects :2
Enter name of student 1 :daniel
Enter mark1 of Student daniel :90
Mark 1 for Student daniel is 90.0
Enter mark2 of Student daniel :80
Mark 2 for Student daniel is 80.0

Enter name of student 2 :roshan
Enter mark1 of Student roshan :99
Mark 1 for Student roshan is 99.0
Enter mark2 of Student roshan :89
Mark 2 for Student roshan is 89.0

Enter name of student 3 :akash
Enter mark1 of Student akash :99
Mark 1 for Student akash is 99.0
Enter mark2 of Student akash :99
Mark 2 for Student akash is 99.0
"""
        
        