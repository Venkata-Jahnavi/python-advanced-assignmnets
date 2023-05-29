#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment23


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. If you have any, what are your choices for increasing the comparison between different figures on the same graph');get_ipython().run_line_magic('pinfo', 'graph')

Answer: A scatter chart shows the relationship between two different variables and it can reveal the distribution trends.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. Can you explain the benefit of compound interest over a higher rate of interest that does not compound after reading this chapter');get_ipython().run_line_magic('pinfo', 'chapter')

Answer: IDK what chapter it is talking about but in general sense Compound interest causes one's wealth to grow faster. It makes a sum of money grow at a faster rate than simple interest because one will earn returns on the money other invest, as well as on returns at the end of every compounding period. This means that one don't have to put away as much money to reach others goals.


# In[ ]:





# In[ ]:


Q3. What is a histogram, exactly? Name a numpy method for creating such a graph.

Answer: A histogram displays numerical data by grouping data into "bins" of equal width. Each bin is plotted as a bar whose height corresponds to how many data points are in that bin. Bins are also sometimes called "intervals", "classes", or "buckets".

NumPy.histogram() Method in Python can be used.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. If necessary, how do you change the aspect ratios between the X and Y axes');get_ipython().run_line_magic('pinfo', 'axes')

Answer:


# In[1]:



import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0,math.pi,0.01)
y = np.sin(20*x)

plt.figure(figsize = (5,4))
plt.plot(x,y)
plt.title('plot with undefined aspect ratio')
plt.show()


# In[2]:



plt.figure(figsize=(10,3))
plt.plot(x,y)
plt.title('plot with undefined aspect ratio')
plt.show()


# In[3]:


plt.figure(figsize=(10,3)) #fig size same as before
ax = plt.gca() #we first need to get the axis handle
ax.set_aspect(1.5) #sets the height to width ratio to 1.5. 
#Use help(ax.set_aspect) for more options.

plt.plot(x,y)
plt.title('plot with Fixed aspect ratio')
plt.show()


# In[ ]:





# In[ ]:


Q5. Compare and contrast the three types of array multiplication between two numpy arrays: dot product, outer product, and regular multiplication of two numpy arrays.

Answer: In Python if we have two numpy arrays which are often referred as a vector. The ‘*’ operator and numpy.dot() work differently on them.


# In[4]:


import numpy as np


# vector v1 of dimension (2, 2)
v1 = np.array([[1, 2], [1, 2]])

# vector v2 of dimension (2, 2)
v2 = np.array([[1, 2], [1, 2]])

print("vector multiplication")
print(np.dot(v1, v2))
print("outer multiplication")
print(np.outer(v1, v2))
print("\nElementwise multiplication of two vector")
print(v1 * v2)


# In[5]:


import numpy as np


v1 = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

v2 = np.array([[[1, 2, 3], [1, 2, 3], [1, 2, 3]]])

print("vector multiplication")
print(np.dot(v1, v2))
print("outer multiplication")
print(np.outer(v1, v2))
print("\nElementwise multiplication of two vector")
print(v1 * v2)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. Before you buy a home, which numpy function will you use to measure your monthly mortgage payment');get_ipython().run_line_magic('pinfo', 'payment')

Answer: In order to calculate the monthly mortgage payment, we canuse the numpy function . pmt(rate, nper, pv) where: rate = The periodic (monthly) interest rate. nper = The number of payment periods (months) in the lifespan of the mortgage loan.

np.pmt()


# In[ ]:


Q7. Can string data be stored in numpy arrays? If so, list at least one restriction that applies to this data.

Answer: we can store string and then we can use arbitary length at aa place of missing values in givn array. genrally if they are all of same length it is preferred.


# In[6]:



# importing the numpy library as np
import numpy as np

# Create a numpy array
# set the dtype to object
country = np.array(['USA', 'Japan', 'UK', '', 'India', 'China'], dtype = 'object')

# Print the array
print(country)


# In[7]:



#Now we can use assign a value of arbitrary length at the place of missing value in the given array.

# Assign 'New Zealand' to the missing value
country[country == ''] = 'New Zealand'
  
# Print the array
print(country)


# In[ ]:





# In[ ]:




