import time
import math
import matplotlib.pyplot as plt
from numpy import append

timev=[]
number=[]

def GCD(x):
     
    return(math.gcd(2,x))
    

for i in range(200,600):
    num=int(i)
    number.append(i)
    
    begin=time.perf_counter()
    GCD(i)
    end=time.perf_counter()
    timev.append(end-begin)
    
    
plt.plot(number,timev)
plt.xlabel("time")
plt.ylabel("number")
plt.show()

