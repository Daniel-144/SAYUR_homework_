# We have 3 colleges - each college has a different cut off mark for engineering college admission.
# Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
# For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
# for admission in College 1 and College 2
mark1=int(input('enter the mark1'))
mark2=int(input('enter the mark2'))
mark3=int(input('enter the mark3'))
mark4=int(input('enter the mark4'))
mark5=int(input('enter the mark5'))
# to get rid of runtime errors. i use a if condition which will allow to run the program only if all marks are equal or greater tthan zero
# and less than 100
if (mark1>=0 and mark1<=100) and (mark2>=0 and mark2<=100) and (mark3>=0 and mark3<=100) and (mark4>=0 and mark4<=100) and (mark5>=0 and mark5<=100):
 # to calculate the total marks add the individual marks
 total=mark1+mark2+mark3+mark4+mark5
 #to find the average divide it by 5
 avg=total/5
 college1_cf=93
 college2_cf=89
 college3_cf=97
 print(f'***eligible cutoff***\n college 1={college1_cf} or greater \ncollege 2={college2_cf}\ncollege 3={college3_cf}')
 # to check the eligiblity i had used a if elif condition
 if (avg >= college1_cf and avg >= college3_cf and avg>= college2_cf):
    print(f'his cut off is {avg}. he is eligible for college 1, college 2 and college 3')
 elif(avg >= college1_cf and avg < college3_cf and avg >= college2_cf):
    print(f'his cut off is {avg}. he is eligible for college 1, college 2 ')
 elif(avg >= college1_cf and avg< college2_cf and avg < college3_cf):
    print(f'his cut off is {avg}. he is eligible for only college 1')
 elif(avg < college1_cf and avg < college2_cf and avg < college3_cf):
    print(f'his cut off is {avg} . unfortunately he is not eligible for all the 3 colleges')
else:
    print("invalid input")

