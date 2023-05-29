#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 15


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What are the new features added in Python 3.8 version');get_ipython().run_line_magic('pinfo', 'version')

Answer: Python 3.8 adds some new syntax to the language, a few minor changes to existing behavior, and mostly a bunch of speed improvements — maintaining the tradition from the earlier 3.7 release

Example: PEP 572 (Assignment Expressions) – The walrus operator (:=)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What is monkey patching in Python');get_ipython().run_line_magic('pinfo', 'Python')

Answer: In Python, the term monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time.


# In[1]:


class A:
     def func(self):
          print ("func() is being called")
    


# In[2]:


def monkey_f(self):
	print ("monkey_f() is being called")

# replacing address of "func" with "monkey_f"
monk.A.func = monkey_f
obj = monk.A()

# calling function "func" whose address got replaced with function "monkey_f()"
obj.func()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What is the difference between a shallow copy and deep copy');get_ipython().run_line_magic('pinfo', 'copy')

Answer: A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original. A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What is the maximum possible length of an identifier');get_ipython().run_line_magic('pinfo', 'identifier')

Answer: Identifiers can be a combination of letters, numbers, special symbols, etc. But it must not extend 31 characters. Hence, the maximum possible length of an identifier is 31


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is generator comprehension');get_ipython().run_line_magic('pinfo', 'comprehension')

Answer: A generator comprehension is a single-line specification for defining a generator in Python.


gen = (i**2 for i in range(100))
print(gen)


# In[3]:



gen = (i**2 for i in range(100))
sum(gen)


# In[4]:


gen = (i for i in range(1, 11))
5 in gen


# In[ ]:




