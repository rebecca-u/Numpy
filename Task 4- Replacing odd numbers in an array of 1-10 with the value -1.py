import numpy as np
array= np.array([1,2,3,4,5,6,7,8,9,10])

odd_values = (array%2 == 1)
array[odd_values] = -1
print(array)
