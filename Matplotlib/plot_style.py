from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

x=[5,8,10]
y=[12,16,6]

x1=[6,9,11]
y1=[6,15,7]

plt.plot(x,y,'g',label='lineone',linewidth=5)
plt.plot(x1,y1,label='labeltwo',linewidth=5)

plt.title("ExtraInfo")
plt.ylabel("y-axis")
plt.xlabel("x-axis")

plt.grid(True,color='k')

plt.show()

