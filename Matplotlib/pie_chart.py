from matplotlib import pyplot as plt

slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']

plt.pie(slices,
        labels=activities,
        shadow=True,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%'

)

#explode used to take out one of the pie
#autopct used for mention the percentage of each pie

plt.title("Pie Chart")
plt.show()