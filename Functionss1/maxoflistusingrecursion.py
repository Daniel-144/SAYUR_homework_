def max1(list):
    if len(list) == 1:
        return list[0]
    
    else:
        return (max(list[0],max1(list[1:])))
    

list=[2,10,20,100,0,-1]
n=len(list)
print(max1(list))