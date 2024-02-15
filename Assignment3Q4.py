import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,25,30]
sx=[0.3,3.8,1.2,2.5]
sy=[11,25,9,26]
plt.scatter(sx,sy,color='darkblue',marker='^')
plt.plot(x,y,color='r',linewidth=3)
plt.show()
