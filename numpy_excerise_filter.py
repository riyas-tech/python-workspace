import numpy as np

arr = np.array([1,10,20,30,40])

#filter out elements greater than 10
filtered_array = np.vectorize(lambda x : x +5)([arr])

print("Original Array   :" , arr)
print("Filtered Array   :", filtered_array)