import time
import matplotlib.pyplot as plt
from numpy import append
import random
    	

def mergeSort(i):
    arr = []
    for j in range(0):
     arr.append(random.randint(0,i))
    if len(arr) > 1:
      
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1




if __name__ == "__main__":
    
	timev=[]
	number=[]
	n=0
for i in range(400,1000):
    num=int(i)
    number.append(i)
    
    begin=time.perf_counter()
    mergeSort(i)
    end=time.perf_counter()
    timev.append(end-begin)
      
plt.plot(number,timev)
plt.xlabel("time")
plt.ylabel("number")
plt.show()

    
	

