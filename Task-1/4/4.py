import matplotlib.pyplot as plt
# x=[4,6,8,3,9,4] #Starx
# y=[2,9,2,7,7,2] #Stary
x=[]
y=[]
n = int(input("Enter the no. of coordinates: "))
for i in range(n):
    a = int(input("Enter x-coordinate"+str(i+1)+": "))
    b = int(input("Enter y-coordinate"+str(i+1)+": "))
    x.append(a)
    y.append(b)
plt.plot(x,y)
plt.show()