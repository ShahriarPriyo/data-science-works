import  numpy as np

a=np.array([(1,2,3),(4,5,6)])
b=np.array([(4,5,6),(7,8,9)])

print(np.vstack((a,b)))
#vertical stack
print(np.hstack((a,b)))


print(a.ravel())
#convert the array into one column