#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 7


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the purpose of the try statement');get_ipython().run_line_magic('pinfo', 'statement')

Answer: The try statement allows a programmer to define a block of code to be tested for errors while it is being executed. The catch statement allows you to define a block of code to be executed, if an error occurs in the try block.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What are the two most popular try statement variations');get_ipython().run_line_magic('pinfo', 'variations')

Answer:

Variation 1:

try: # Some Code except: # Executed if error in the # try block

Variation 2:

try: # Some Code except: # Executed if error in the # try block else: # execute if no exception

Variation 3:

try: # Some Code except: # Executed if error in the # try block else: # execute if no exception finally: # Some code .....(always executed)


# In[ ]:





# In[ ]:


Q3. What is the purpose of the raise statement? Answer: The raise keyword is used to raise an exception. We can define what kind of error to raise, and the text to print to the user.


# In[1]:



#raising an exception 
input = input("Enter the input:")
if not type(input) is int:
  raise TypeError("Only integers are allowed") #exception will be thrown
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What does the assert statement do, and what other statement is it like');get_ipython().run_line_magic('pinfo', 'like')

Answer: An assert statement checks whether a condition is true. If a condition evaluates to True, a program will keep running. If a condition is false, the program will return an AssertionError. At this point, the program will stop executing. Assertion is like raise statement.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is the purpose of the with/as argument, and what other statement is it like');get_ipython().run_line_magic('pinfo', 'like')

Answer: The with statement in Python is used for resource management and exception handling. We use it while working with file streams. For example, the statement ensures that the file stream process doesn't block other processes if an exception is raised, but terminates properly. We can use a try statement or block it is somewhat similar to with.


# In[ ]:




