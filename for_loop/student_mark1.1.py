######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67
#initializing a list to store the marks
mark_list = []
number_of_students=int(input("Enter number of students :"))
#get the name of the student 1 as input 
name=input("enter the name of student 1 :")
for mark in range(2):
    marks=float(input(f"enter mark{mark+1} of student {name}: "))
    #storing the marks of the student in the mark list
    mark_list.append(marks)
print(f"{name}'s mark's {mark_list[mark-1]},{mark_list[mark]}")
print("")
# loop for other students
for student in range (1,number_of_students):
    name=input(f"Enter name of student {student+1} :")
    for mark in range(2):
        marks=float(input(f"Enter mark{mark+1} of Student {name} :"))#use formatted string 
        # the elements of the list is changed
        mark_list[mark]=marks
    print(f"{name}'s mark's  {mark_list[mark-1]},{mark_list[mark]}")    
    print("") 

"""
OP
Enter number of students :1         |
enter the name of student 1 :daniel |
enter mark1 of student daniel: 89   |
enter mark2 of student daniel: 76   |
daniel's mark's 89.0,76.0           |
"""
"""
OP:
Enter number of students :3
enter the name of student 1 :daniel
enter mark1 of student daniel: 57
enter mark2 of student daniel: 89
daniel's mark's 57.0,89.0

Enter name of student 2 :akash
Enter mark1 of Student akash :90
Enter mark2 of Student akash :80
akash's mark's  90.0,80.0

Enter name of student 3 :roshan
Enter mark1 of Student roshan :90
Enter mark2 of Student roshan :90
roshan's mark's  90.0,90.0
"""
        

    
    