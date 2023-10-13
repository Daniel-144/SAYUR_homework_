"""
3. Accept 2 integers. print all Nos which are miror nos falling 
between the given range.
eg: first no 300  
second no: 400
303,313,323,.....393
"""

#getting the starting range and ending range from the user
start=int(input("enter the starting range: "))
end=int(input("enter the ending range: "))
# initializing a empty list to store all the miror numbers in the range.
MirorNumber=[]
#  loop to find the miror numbers.
for no in range(start,end+1):
    answer=0
    temp=no
    while temp!=0:
        remainder=temp %10
        answer = (answer * 10)+ remainder
        temp=temp//10
    if no == answer:
        MirorNumber.append(answer)
print(f"the list of mirror numbers:{MirorNumber}")

"""
OP
enter the starting range: 300
enter the ending range: 400
the list of mirror numbers:[303, 313, 323, 333, 343, 353, 363, 373, 383, 393]
"""