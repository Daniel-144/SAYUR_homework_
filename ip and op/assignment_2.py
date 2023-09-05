def balance_calculation(a,b,c,d,e,f,g,h,i,j,sp,tot):
    balance=tot-sp
    print("total amount :",tot)
    print("spent amount is: ", sp)
    print("balance amount is : ", balance)
    balance_a = balance*(a / tot)
    balance_b = balance * (b / tot)
    balance_c = balance*(c / tot)
    balance_d = balance * (d / tot)
    balance_e = balance * (e / tot)
    balance_f = balance * (f / tot)
    balance_g = balance * (g / tot)
    balance_h = balance * (h / tot)
    balance_i = balance * (i / tot)
    balance_j = balance * (j / tot)
    print("the balance of student 1 is ",balance_a)
    print("the balance of student 2 is ", balance_b)
    print("the balance of student 3 is ", balance_c)
    print("the balance of student 4 is ", balance_d)
    print("the balance of student 5 is ", balance_e)
    print("the balance of student 6 is ", balance_f)
    print("the balance of student 7 is ", balance_g)
    print("the balance of student 8 is ", balance_h)
    print("the balance of student 9 is ", balance_i)
    print("the balance of student 10 is ", balance_j)

student_1=(int(input("enter the the amount for student 1:")))
student_2=(int(input("enter the the amount for student 2:")))
student_3=(int(input("enter the the amount for student 3:")))
student_4=(int(input("enter the the amount for student 4:")))
student_5=(int(input("enter the the amount for student 5:")))
student_6=(int(input("enter the the amount for student 6:")))
student_7=(int(input("enter the the amount for student 7:")))
student_8=(int(input("enter the the amount for student 8:")))
student_9=(int(input("enter the the amount for student 9:")))
student_10=(int(input("enter the the amount for student 10:")))
total=student_1+student_2+student_3+student_4+student_5+student_6+student_7+student_8+student_9+student_10
spent=(int(input("enter the spent amount: ")))
if spent>total:
    print("print amount is greater")
else:
    balance_calculation(student_1,student_2,student_3,student_4,student_5,student_6,student_7,student_8,student_9,
                        student_10,spent,total)






