#Numpy Intro
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))

#0-D arrays
arr = np.array(42)

#1-D arrays
arr = np.array([1,2,3,4,5])

#2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#Check arrays number of dimensions
print(arr.ndim)

#Higher dimension arrays
arr = np.array([1,2,3,4],ndmin=5)
print(arr.ndim)

## NumPy Array Indexing
arr = np.array([1,2,3,4])
print(arr[0])

#Access 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1,0])

#Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr[1,1,2])

#Negative Indexing
arr = np.array([1,2,3,4])
print(arr[-1])

##NumPy Array Slicing
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step]
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[:5])
print(arr[1:])
print(arr[:])
print(arr[:-1])

#Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

#Get the data type of an array object
print(arr.dtype)

#Create an array with data type string
str_array = np.array([1,2,3,4,5], dtype='S')
print(str_array.dtype)

#Create an array with data type 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Change data type from float to integer by using 'i' as parameter value
arr = np.array([1.1,1.2,1.3])
print(arr.dtype)
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# NumPy Array Copy vs View

# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


# Print the shape of a 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6],[4, 5, 6]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print('shape of the array: ', arr.shape)

# Reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr.shape)
