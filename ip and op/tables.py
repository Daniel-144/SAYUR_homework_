"""""
to print the given table
"""
end=int(input('enter the ending point of the table:'))
for i in range(1,end+1):
       print(f'table {i}')
       for j in range(end+1):
         result=i*j
         print(f'{i}*{j}={result}')
       print("\n")
print('end of tables')