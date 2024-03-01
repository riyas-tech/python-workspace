import numpy as np

arr = np.array([1,10,20,30,40])

#filter out elements greater than 10
filtered_array = np.vectorize(lambda x : x +5)([arr])

print("Original Array   :" , arr)
print("Filtered Array   :", filtered_array)

print(np.random.randint(1,100))

# create an array of 10 zeros 
print(np.zeros(10))

# create an array of 10 ones 
print(np.ones(10))

# create an array of 10 fives
print(np.full(10, 5))

# create an array of integers from 10 to 50
print(np.arange(10,51))

# create an array full of even integers from 10 to 50
print(np.arange(10,51,2))

# create a 3*3 matrix with values from 0 to 8
values = np.arange(9)
print(values.reshape((3,3)))

# use numpy to generate a random number between 0 and 1
print(np.random.rand())

#use numpy to generate an array of 25 random numbers sampled from a standard normal distribution 
print(np.random.randn(25))

# create an array of 20 linearly spaced numbers between 0 and 1
print(np.linspace(0,1,20))

print(np.arange(1,26).reshape(5,5))

# get the sum of all the values in a matrix
mat = np.arange(1,26).reshape(5,5)
print(np.sum(mat))