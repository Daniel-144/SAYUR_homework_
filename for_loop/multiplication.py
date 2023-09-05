"""
######## Problem  4  ###############

#print a multiplication table like below.
#get user intput for start and end numbers. 
#the following example uses 1 to 5.

     1  2  3  4  5
  ********************
1 |  1  2  3  4  5
2 |  2  4  6  8 10
3 |  3  6  9 12 15
4 |  4  8 12 16 20
5 |  5 10 15 20 25
"""
# getting row and column limit from the user
row=int(input('enter the row limit:'))
column=int(input('enter the column limit:'))
# initializing temprovary variables as zero
temp=0
temp2=0
print(" " , end="  ")
for i in range(column):
    print(i+1,end="  ")
print("\n",end="  ")
print("*"*20)

for j in range(1,row+1):
    for k in range(column+1):
      if(k==0):
         print(temp2+1,end=" | ")
         temp2+=1
      else:
         print(j*k,end="  ")
    print("")

"""
O/P:
enter the row limit:6
enter the column limit:5
   1  2  3  4  5
  ********************
1 | 1  2  3  4  5
2 | 2  4  6  8  10
3 | 3  6  9  12  15
4 | 4  8  12  16  20
5 | 5  10  15  20  25
6 | 6  12  18  24  30
"""
      
        
    
           


