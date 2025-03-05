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

#-- multidiemsional numpy array
"""
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
print('Shape: ', numpy_two_dimensional_list.shape)
print('Size: ', numpy_two_dimensional_list.size)
print('Data type: ', numpy_two_dimensional_list.dtype)
"""

#-- getting items from numpy array
first_row=numpy_two_dimensional_list[0]
second_row=numpy_two_dimensional_list[1]
third_row=numpy_two_dimensional_list[2]

first_column= numpy_two_dimensional_list[:,0]
second_column = numpy_two_dimensional_list[:,1]
third_column = numpy_two_dimensional_list[:,2]
"""
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)

print('Full array: ',numpy_two_dimensional_list)
"""
#-- slice numpy array
first_two_rows_and_columns = numpy_two_dimensional_list[0:2, 0:2]
"""
print(first_two_rows_and_columns)
"""
##-- reverse array
"""
print('invertido x1: \n',numpy_two_dimensional_list[::-1])
print('invertido x2: \n',numpy_two_dimensional_list[::-1,::-1])
"""

#-- represent missing values

"""print(numpy_two_dimensional_list)
numpy_two_dimensional_list[1,1] = 55
numpy_two_dimensional_list[1,2] =44
print(numpy_two_dimensional_list)"""

##-- numpy zeroes
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
numpy_ones = np.ones((3,3),dtype=int,order='C')
doses=numpy_ones*2
"""
print(numpy_zeroes)
print(numpy_ones)
print(doses)
"""
##-- reshape
first_shape  = np.array([(1,2,3), (4,5,6)])
reshaped = first_shape.reshape(3,2)
flattened= reshaped.flatten()
"""
print(first_shape)
print(reshaped)
print(flattened)
"""

## --Horizontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
"""
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
"""
## -- vertical stack
"print('Vertical Append: \n', np.vstack((np_list_one, np_list_two)))"

#-- Generar numeros random
random_float = np.random.random()
random_floats = np.random.random(5)
random_int = np.random.randint(0, 11)
random_ints = np.random.randint(2,10, size=4)
random_int_arr = np.random.randint(2,10, size=(3,3))
rand_int = np.random.randint(0, 10, size=[5,3])
"""
print(random_float)
print(random_floats)
print(random_int)
print(random_ints)
print(random_int_arr)
print(rand_int)
"""

## np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
"print(normal_array)"

#-- random strings

"print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))"

#-- Numpy and statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#counts, bins, _ = plt.hist(normal_array, color="grey", bins=50)
"""
print("Resultado del histograma:")
print(counts)
print(bins)
"""
#-- Matrix en numpy

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
"print(four_by_four_matrix)"
np.asarray(four_by_four_matrix)[2] = 2
"print(four_by_four_matrix)"

#-- Numpy arrange
##-- python range | range(starting, stop, step)
lst = range(0, 11, 2)
"print(lst)"

for l in lst:
    "print(l)"

##-- numpy range | numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
natural_numbers = np.arange(1, 20, 1)
odd_numbers = np.arange(1, 20, 2)
even_numbers = np.arange(2, 20, 2)
"""
print('numeros enteros: \n',whole_numbers)
print('numeros naturales: \n',natural_numbers)
print('numeros impares: \n',odd_numbers)
print('numeros pares: \n',even_numbers)
"""

#-- secuencia de numeros con linspace

arr= np.linspace(1.0, 5.0, num=10)
"print(arr)"

arr=np.linspace(1.0, 5.0, num=5, endpoint=False)
"print(arr)"

## LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.
## numpy.logspace(start, stop, num, endpoint)

log=np.logspace(2, 4.0, num=4)
"print(log)"

## to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
"""
print(x)
print(x.itemsize)
"""

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
"""
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])
"""


#------Numpy Functions
"""
    Min np.min()
    Max np.max()
    Mean np.mean()
    Median np.median()
    Varience
    Percentile
    Standard deviation np.std()
"""

## min, max, mean, median, sd
"""
print('min: ', numpy_two_dimensional_list.min())
print('max: ', numpy_two_dimensional_list.max())
print('mean: ',numpy_two_dimensional_list.mean())
print('median: ', np.median(numpy_two_dimensional_list))
print('sd: ', numpy_two_dimensional_list.std())
"""
"""
print(numpy_two_dimensional_list)
print('Column with minimum: ', np.amin(numpy_two_dimensional_list,axis=0))
print('Column with maximum: ', np.amax(numpy_two_dimensional_list,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(numpy_two_dimensional_list,axis=1))
print('Row with maximum: ', np.amax(numpy_two_dimensional_list,axis=1))
"""

## idk

np_normal_dis = np.random.normal(5, 0.5, 1000)
"""
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
#print('mode: ', stats.mode(np_normal_dis)) | from scipy import stats(instalar)
print('sd: ', np.std(np_normal_dis))
"""

#-- graphs
#plt.hist(np_normal_dis, color="grey", bins=21)
"plt.show()"

"""
numpy.dot(): Dot Product in Python using Numpy
Dot Product
Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

Syntax

numpy.dot(x, y, out=None)
"""

## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])

### 1*4+2*5 + 3*6
result= np.dot(f, g)
"print(result)"

### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
result=np.matmul(h, i)
"print(result)"

## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
result= np.linalg.det(i)
"print(result)"

#-- random numpy array mod

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
"print(Z)"

#--
new_list = [ x + 2 for x in range(0, 11)]
"print(new_list)"

np_arr = np.array(range(0, 11))
np_arr + 2
"print(np_arr)"

#-- We use linear equation for quantities which have linear relationship. Let's see the example below:

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
"print(pressure)"
"""
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
"""

#-- graph gausiana con numpy
"""
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
"""




