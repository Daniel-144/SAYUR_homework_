"""
write a program for collatz_conjecture.
# Collatz_conjecture means - start with input number.
# for even number , divide by 2(n/2)
# for odd number - 3n+1
# apply the above for the result number until the answer number is 1.
# print the number which became 1 in minimum number of iteration.
"""
num=[]
count=[]
for i in range(0,2):
    num.append(int(input(f"enter the number{i+1}: ")))
for n in num:
    time=0
    while n != 1:
        time+=1 # to count the number of iteration
        if  n % 2 == 0: 
            n = n // 2  # for even number , divide by 2(n/2)
        else:
            n =(3*n)+1
    count.append(time)
minimum_count=min(count)
print(f"the number {num[count.index(minimum_count)]} has undergone the {minimum_count} times")
