#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 12


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q1. Does assigning a value to a string's indexed character violate Python's string immutability");get_ipython().run_line_magic('pinfo', 'immutability')

Answer: In Python, strings are made immutable so that programmers cannot alter the contents of the object (even by mistake). This avoids unnecessary bugs. we can assign a value to a string's indexed character it doesn't violate Python's string immutability because for ding that we first have to split the string word into characters which leaves us with simple character string we can replace it easily with some other character but still it will be string even if the replaced value will be an interger or floting number or anything.



# In[1]:



str = "as"
print(str.replace("a","1"))
print(type(str.replace("a","1")))


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q2. Does using the += operator to concatenate strings violate Python's string immutability? Why or why not");get_ipython().run_line_magic('pinfo', 'not')

Answer:If you want to concatenate a number, such as an integer int or a floating point float , with a string, convert the number to a string with str() and then use the + operator or += operator. NO, same explanation as above bcause it will still be in string type.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. In Python, how many different ways are there to index a character');get_ipython().run_line_magic('pinfo', 'character')

Answer: Each of a string's characters corresponds to an index number and each character can be accessed using their index number. We can access characters in a String in Two ways :

Accessing Characters by Positive Index Number.
Accessing Characters by Negative Index Number.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What is the relationship between indexing and slicing');get_ipython().run_line_magic('pinfo', 'slicing')

Answer: “Indexing” means referring to an element of an iterable by its position within the iterable. “Slicing” means getting a subset of elements from an iterable based on their indices.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q5. What is an indexed character's exact data type? What is the data form of a slicing-generated substring");get_ipython().run_line_magic('pinfo', 'substring')

Answer: The type in slicing remains the same type in which it is entered. But in indexing the tye may differ. An examle is shown below to explain this.


# In[2]:


l = [1,2,3,4,5]
print(type(l[2]))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What is the relationship between string and character "types" in Python');get_ipython().run_line_magic('pinfo', 'Python')

Answer: In Python, Strings are arrays of bytes representing Unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.


# In[ ]:





# In[ ]:


Q7. Identify at least two operators and one method that allow you to combine one or more smaller strings to create a larger string.

Answer:

operators are + and *

method: format() or join()


# In[ ]:





# In[ ]:



get_ipython().set_next_input('Q8. What is the benefit of first checking the target string with in or not in before using the index method to find a substring');get_ipython().run_line_magic('pinfo', 'substring')

Answer: set() helps us in knowing if there are't any repeatable words or items in the string and returns us a list sor set with only single entry of a particular item.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. Which operators and built-in string methods produce simple Boolean (true/false) results');get_ipython().run_line_magic('pinfo', 'results')

Answer:

operators : = , < , >

methods: bool()


# In[ ]:




