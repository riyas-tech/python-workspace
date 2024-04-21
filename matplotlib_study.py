import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2
print(x)
print(y)

# plt.plot(x,y, 'r-')
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')
# plt.show()

#Object oriented methods 
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')

fig,axes = plt.subplots(nrows=1, ncols=2)

plt.show()
