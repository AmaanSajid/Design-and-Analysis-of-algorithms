import time
import matplotlib.pyplot as plt
from numpy import append

timev=[]
number=[]

def factorial(n):
     
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
    

for i in range(200,600):
    num=int(i)
    number.append(i)
    
    begin=time.perf_counter()
    factorial(i)
    end=time.perf_counter()
    timev.append(end-begin)
    
    
plt.plot(number,timev)
plt.xlabel("time")
plt.ylabel("number")
plt.show()

