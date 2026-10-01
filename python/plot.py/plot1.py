import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=[0,1,2,3,4]
y=[0,2,4,6,8]
#plt.plot(x,y,label='2x',color='b',linewidth=2,linestyle='--', marker='.',markersize=10,markeredgecolor='y')
#use shorthand notation
#fmt='[color],[marker],[line]
plt.plot(x,y,'b^--',label='2x')

##line number two
x2=np.arange(0,4.5,0.5)
plt.plot(x2[:6],x2[:6]**2,'r',label='x^2')
plt.plot(x2[5:],x2[5:]**2,'r--')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title("My First Graph!" ,fontdict={'fontname':'Comic sans MS' ,'fontsize':20})
plt.xticks([0,1,2,3])
plt.yticks([0,2,4,6,8,10])
plt.legend()
plt.show()