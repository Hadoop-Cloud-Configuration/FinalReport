import numpy as np  
import matplotlib.pyplot as plt  
   
n_groups = 2  
means_men =(44.2,45)  
means_women = (30.94,34)  
    
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
