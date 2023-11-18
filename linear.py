def linearsec(list1,N,key):
    for i in range(0,N):
        if(list1[i]==key):
            return i
    return -1
    
    
list1 = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input("input the numbers in list"))
  
    list1.append(ele)
    
key=int(input("assign the value to be found"))
ans=linearsec(list1,key,n)
if ans==-1:
    print(key,"is not found in array")
else:
    print(key,"is found in the array")
    