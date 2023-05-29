#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 10


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the difference between getattr and getattribute');get_ipython().run_line_magic('pinfo', 'getattribute')

Answer: getattribute: Is used to retrieve an attribute from an instance. getattr: Is executed as the last resource when attribute is not found in an object.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What is the difference between properties and descriptors');get_ipython().run_line_magic('pinfo', 'descriptors')

Answer: Descriptors are a low-level mechanism that lets us hook into an object's attributes being accessed. Properties are a high-level application of this. that is, properties are implemented using descriptors.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What are the key differences in functionality between getattr and getattribute, as well as properties and descriptors');get_ipython().run_line_magic('pinfo', 'descriptors')

Answer: A key difference between getattr and getattribute is that getattr is only invoked if the attribute wasn't found the usual ways. It's good for implementing a fallback for missing attributes and is probably the one of two you want.

