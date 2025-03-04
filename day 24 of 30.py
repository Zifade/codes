#Repeat all the examples

import numpy as np
"""
print('numpy:', np.__version__)
print(dir(np))
"""
#-- crear numpy array int
python_list=[1,2,3,4,5]

numpy_array_int= np.array(python_list)
"""print(numpy_array_int)"""

#-- crear numpy array float
python_list = [1,2,3,4,5]

numy_array_float = np.array(python_list, dtype=float)
"""print(numy_array_float)"""

#-- crear numpy array boolean
numpy_array_bool = np.array([0, 1, -1, 0, 0], dtype=bool)
"""print(numpy_array_bool)"""

#-- crear numpy array multidimensional
two_dimensional_list=[[1,2,3],[4,5,6],[7,8,9]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
"""print(numpy_two_dimensional_list)"""

#-- convert numpy array to list
"""print('de numpy a list: ', numpy_two_dimensional_list.tolist())"""

#-- numpy array from tuple
py_tuple=(1,2,3,4,5)
tuple_to_numpy_array= np.array(py_tuple)

"""
print(py_tuple)
print(tuple_to_numpy_array)
"""

#-- shape of numpy array
nums = np.array([1, 2, 3, 4, 5])
hs=np.array([[1,2,3,4],[5,6,7,8]])
"""
print(nums)
print('shape of nums: ', nums.shape)
print('shape of two dimensions: ',numpy_two_dimensional_list.shape)
print('halfs shape: ',hs.shape)
"""
#-- data type in numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
"""
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
"""

#-- length pero en numpy(size)
"""
print('size: ', nums.size)
print('size: ', hs.size)
"""


#-- operaciones en numpy
"""
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)
"""
"""
print(nums+10)
print((float_array+10)*2/3)
"""

#-- converting data types de numpy arrays
"""
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr)
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)
numpy_bool=np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_bool)
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
print(numpy_int_arr.astype('int').astype('str'))
"""




