list1 = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input("input the numbers in list"))
  
    list1.append(ele)
    
MAX=max(list1)
MIN=min(list1)

print(MAX)
print(MIN)

