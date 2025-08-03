import numpy as np

# Creating a numpy array from a list
array1 = np.array([1, 2, 3, 4])
array2 = np.array([1,2,3],dtype=np.float64)
print("array1:", array1)  # Expected output: [1 2 3 4]
print("array2:", array2)  # Expected output: [1. 2. 3.]

# Get Dimensions of the array
print("Dimensions of array1:", array1.ndim)  # Expected output: 1

# Get Shape of the array
# shape is a tuple representing the size of each dimension (e.g., (rows, columns))
array1 = np.array([1, 2, 3, 4])
array2 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print("Shape of array1:", array1.shape)  # Expected output: (4,)
print("Shape of array2:", array2.shape)  # Expected output: (2, 4)

# Get a specific element from the array
print("Element at index 2 in array1:", array1[2])  # Expected
# for 2d arrays, you can specify row and column indices: as array[row:column]
array3 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print("Element at index (1, 2):", array3[1, 2]) 
print("The first row of array3:", array3[1,:])  # Expected output: [5 6 7 8]
print("The first column of array3:", array3[:,0])  # Expected output: [1 5]

# create a matrix of 1s and 0s
ones_matrix = np.ones((2, 3))  # 2 rows, 3 columns
zeros_matrix = np.zeros((2, 3))  # 2 rows, 3 columns
print("Ones matrix:\n", ones_matrix)  # Expected output: [[1. 1. 1.] [1. 1. 1.]]
print("Zeros matrix:\n", zeros_matrix)  # Expected output: [[0. 0. 0.] [0. 0. 0.]]

# create a matrix of single numbers
full_matrix = np.full((2, 3), 7)  # 2 rows, 3 columns, filled with 7
print("Full matrix:\n", full_matrix)  # Expected output: [[7 7 7] [7 7 7]]

# create an identity matrix
identity_matrix = np.identity(3)  # 3x3 identity matrix
print("Identity matrix:\n", identity_matrix)  # Expected output: [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]]
