########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

string=input("enter a string:")
i=0
n=len(string)
while(i<n):
    stri=0
    print(" "*(n-i),end="")
    while(stri<=i):
        print(string[stri],end=" ")
        stri+=1
    i+=1
    print()
i=0
while(i<n):
       stri=0
       print(" "*(i),end=" ")
       while(stri<n-i):
              print(string[stri],end=" ")
              stri+=1
       i+=1
       print()

"""
OP
enter a string:ram 
   r 
  r a 
 r a m 
 r a m 
  r a 
   r
"""
"""
enter a string:ronaldo
       r
      r o
     r o n
    r o n a
   r o n a l
  r o n a l d
 r o n a l d o
 r o n a l d o
  r o n a l d
   r o n a l
    r o n a
     r o n
      r o
       r
"""