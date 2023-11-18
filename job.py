profit=[25,90,45,70,35,65,80,40,51]
job=[7,3,1,5,2,4,5,3,5]
maxi=0;
for i in range(0,len(profit)):
    for j in range(0,len(profit)):
        if profit[i]>profit[j]:
            temp=profit[i];
            profit[i]=profit[j]
            profit[j]=temp
            temp1=job[i];
            job[i]=job[j]
            job[j]=temp1
#print(profit)
#print(job)

job1=[]
for i in range(0,len(profit)):
    for i in range(0,len(profit)):
        if job[i]==job[j]:
            if profit[i]>profit[j]:
                job1[job[i]]=job[i]
            else:
                job1[job[j]]=job[j]
            

    
        
    