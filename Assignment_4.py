#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment_4


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1.Which two operator overloading methods can you use in your classes to support iteration');get_ipython().run_line_magic('pinfo', 'iteration')

Answer: init, str are two operator overloading methods can which can be used to support iteration.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. In what contexts do the two operator overloading methods manage printing');get_ipython().run_line_magic('pinfo', 'printing')

Answer: They can mamnage priting or outputting values wuth return statements.

In cases where the str() method is not defined, Python uses the repr() method to print the object, as well as to represent the object when str() is called on it.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. In a class, how do you intercept slice operations');get_ipython().run_line_magic('pinfo', 'operations')

Answer: Shown below-


# In[1]:


sliced ='ashish kumar singh'.__getitem__(slice(0, 8, 1)) #using slice() and __getitem__ slicing can be achieved in class
print(sliced)
     


# In[2]:


class Demo:
	def __getitem__(self, key):
		# print a[1], a[1, 2],
		# a[1, 2, 3]
		print(key)
		#return key

a = Demo()
a[1]
a[1, 2]
a[1, 2, 3]


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. In a class, how do you capture in-place addition');get_ipython().run_line_magic('pinfo', 'addition')

Answer: Python provides the operator x += y to add two objects in-place by calculating the sum x + y and assigning the result to the first operands variable name x. We can set up the in-place addition behavior for our own class by overriding the magic “dunder” method iadd(self, other) in our class definition.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. When is it appropriate to use operator overloading');get_ipython().run_line_magic('pinfo', 'overloading')

Answer: The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class. Hence when we have to extended meaning beyond their predefined operational meaning we can use operator overloading,


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




