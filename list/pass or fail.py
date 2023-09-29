"""
you have a list of students name and another list with their marks in cs.
hard code the values. no need to get as a input.
pass mark 50.
print a new list with all the  students with pass mark along with their marks in format name : marks
also print the students who have failed.
"""
StudentName=['seetha','ram','gopal','lakshmi','sam']
StudentMark=[34,56,78,23,90]
PassMark=50
failcount=0
# initializing a list to store the students with passmark
PassList=[]
# loop to find the number of students who got fail mark and to store the name and mark of students with pass mark in a list
for mark in range(len(StudentMark)):
    if StudentMark[mark]>=50:
        # if student got pass mark in all subjects their mark and their name are stored in a list.
        PassList.append(StudentName[mark]+':'+str(StudentMark[mark]))
    else:
        failcount+=1

print(f"pass student's name and markks:{PassList}")
print(f"No of student's failed:{failcount}")




    
