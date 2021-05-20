import numpy as np

#Create a 1D array of numbers from 0 to 9
array = np.array([0,1,2,3,4,5,6,7,8,9])
print(array)

#Convert a 1D array to a 2D array with 2 rows
new_array = array.reshape(2,5) 
# rows then columns when creating the matrix
print(new_array)
