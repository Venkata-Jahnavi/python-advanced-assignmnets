#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment_22


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What are the benefits of the built-in array package, if any');get_ipython().run_line_magic('pinfo', 'any')

Answer: The Array is much more rigid. That is, the items that an array contains must be of the same type. Therefore, the size of the item will also be the same. We can check the size of each item.


# In[ ]:





# In[ ]:



get_ipython().set_next_input("Q2. What are some of the array package's limitations");get_ipython().run_line_magic('pinfo', 'limitations')

Answer: An array which is formed will be homogeneous.

While declaring an array, passing size of an array is compulsory, and the size must be a constant.

Shifting is required for insertion or deletion of elements in an array


# In[ ]:





# In[ ]:


Q3. Describe the main differences between the array and numpy packages.

Answer: A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. A list is the Python equivalent of an array, but is resizeable and can contain elements of different types. The answer to above query the main difference in two is of performance.


# In[ ]:





# In[ ]:


Q4. Explain the distinctions between the empty, ones, and zeros functions.

Answer: The only difference between numpy.empty numpy.ones and numpy.zeros is that empty uses malloc and zeros uses calloc. Also zeros() and ones() are the NumPy library functions to create two different arrays. zeros() function is used to create an array based on the particular shape and type. All array elements are initialized to 0, which is created by the zeros() function. ones() function works like the zeros() function.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. In the fromfunction function, which is used to construct new arrays, what is the role of the callable argument');get_ipython().run_line_magic('pinfo', 'argument')

Answer: fromfunction() function construct an array by executing a function over each coordinate and the resulting array, therefore, has a value fn(x, y, z) at coordinate (x, y, z). Parameters : function : [callable] The function is called with N parameters, where N is the rank of shape.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What happens when a numpy array is combined with a single-value operand (a scalar, such as an int or a floating-point value) through addition, as in the expression A + n');get_ipython().run_line_magic('pinfo', 'n')

Answer:


# In[1]:


import numpy as np

arr = np.array((1, 2, 3, 4, 5))

print(arr + 1)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. Can array-to-scalar operations use combined operation-assign operators (such as += or *=)? What is the outcome');get_ipython().run_line_magic('pinfo', 'outcome')

Answer: NO


# In[2]:



#using scalar operations error came
import numpy as np

arr = np.array((1, 2, 3, 4, 5))
a = arr += 1
print(a)
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. Does a numpy array contain fixed-length strings? What happens if you allocate a longer string to one of these arrays');get_ipython().run_line_magic('pinfo', 'arrays')

Answer: NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original. The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. if longer strings is allocateed it might cause a computation problem basically increse the time complexity.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. What happens when you combine two numpy arrays using an operation like addition (+) or multiplication (*)? What are the conditions for combining two numpy arrays');get_ipython().run_line_magic('pinfo', 'arrays')

Answer:


# In[3]:



import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = arr1+arr2
arr1 = arr1*arr2

print(arr)
print("\n",arr1)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q10. What is the best way to use a Boolean array to mask another array');get_ipython().run_line_magic('pinfo', 'array')

Answer: Boolean masking is typically the most efficient way to quantify a sub-collection in a collection. Masking in python and data science is when you want manipulated data in a collection based on some criteria. The criteria you use is typically of a true or false nature, hence the boolean part.

Using masked_where() function: Pass the two array in the function as a parameter then use numpy. ma. masked_where() function in which pass the condition for masking and array to be masked.

Using masked_where(), getmask() and masked_array() function: Pass the two array in the function as a parameter then use numpy. ma.
    


# In[ ]:





# In[ ]:


Q11. What are three different ways to get the standard deviation of a wide collection of data using both standard Python and its packages? Sort the three of them by how quickly they execute.

Answer: one method is shown below standar then we can use pandas or using srpiting line by line to ding standard deviation. using pandas std() is generally nicer way and faster.


# In[4]:


import math
def variance(data, ddof=0):
  n = len(data)
  mean = sum(data) / n
  return sum((x - mean) ** 2 for x in data) / (n - ddof)


def stdev(data):
  var = variance(data)
  std_dev = math.sqrt(var)
  return std_dev

stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])

     
2.4


# In[ ]:





# In[ ]:


Q12. What is the dimensionality of a Boolean mask-generated array? Answer: it remain the same. Example below:


# In[5]:


import numpy as np

arr = np.asarray([[[[1, 11], [2, 22], [3, 33]],
                   [[4, 44], [5, 55], [6, 66]]],
                  [[[7, 77], [8, 88], [9, 99]],
                   [[0, 32], [1, 33], [2, 34]]]])

masked_arr = np.ma.masked_less(arr, 3)

print(masked_arr)


# In[ ]:




