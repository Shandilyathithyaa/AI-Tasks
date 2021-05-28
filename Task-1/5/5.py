from matplotlib import pyplot as plt
import pandas as pd
from math import log
x=[]
y=[]
for i in range(1,101):
    x.append(i)
    y.append(x[i-1]**2 + log(x[i-1]/2))
with open("input.csv",'w') as f:
    f.write("x,y\n")
    for i in range(100):
        f.write(str(x[i])+','+str(y[i])+'\n')
sample_data = pd.read_csv('input.csv')
plt.title("y = x^2 + log(x/2)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(sample_data.x,sample_data.y)
plt.show()