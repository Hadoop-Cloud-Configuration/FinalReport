import numpy as np  
import matplotlib.pyplot as plt  
import math
import operator
from datetime import datetime
 
xn=[]
y1=[]
y2=[]

arr = []

class stat():
    def __init__(self, startTime,endTime, duration):
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
    
        
oldfile='no_scaling_pi.csv'
i=0
with open(oldfile, 'r') as infile:
    for line in infile:
 #       xn.append(i)
 #       i=i+1
        data=line.split(',')
#        y1.append(int(data[0]))
#        y2.append(int(data[1]))
        arr.append(stat(int(data[0]), int(data[1]), int(data[2])) )

arr.sort(key=lambda x: x.startTime)



for currentdata in arr:
    i=i+1
 
    y1.append(currentdata.startTime/1000)
    y2.append(currentdata.endTime/1000)
    
ysmin=min(y1)
yemax=max(y2)

for datay in y1:
   xn.append((datay-ysmin))
   
duration=(yemax-ysmin)/1000
print duration
for i in range(len(xn)):
    x = [y1[i]-ysmin,y2[i]-ysmin]
    y = [xn[i],xn[i]]
    #print x
    #print y
    plt.plot(x,y)


plt.xlabel('Duration(s)',fontsize=20)
plt.ylabel('Start Time(s)',fontsize=20)  
plt.title('Run Pi Example without scaling',fontsize=20)
#plt.xlim(0,20)
#plt.ylim(0,20)
plt.show()

'''
print mean
print std
fig, ax = plt.subplots()  
index = np.arange(n_groups)  
bar_width = 0.2  
   
opacity = 0.8  
rects1 = plt.bar(0.8+index, means_men, bar_width,alpha=opacity, color='b',label='Six nodes')  
rects2 = plt.bar(0.8+index + bar_width, means_women, bar_width,alpha=opacity,color='r',label='Eight nodes')  

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

 
plt.ylabel('Percentage',fontsize=20)  
plt.title('Scaling out Comparison for Pi Calculator example',fontsize=20)  
plt.xticks(0.8+index + bar_width, ('CPU usage', 'Memory usage'))  
plt.xlim(0,3)
plt.ylim(0,80)  
leg=plt.legend()
for t in leg.get_texts():
    t.set_fontsize(15)  
   
plt.tight_layout()  
plt.show()
'''
