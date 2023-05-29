#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 13


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. Can you create a programme or function that employs both positive and negative indexing? Is there any repercussion if you do so');get_ipython().run_line_magic('pinfo', 'so')

Answers: Below is a basic program showing positive and negative indexing. NO.



# In[1]:


def arun():

  greetings = "arun kumar"
  print(greetings[0]) 
  print(greetings[-1])

arun()
     
a


# In[ ]:





# In[ ]:


Q2. What is the most effective way of starting with 1,000 elements in a Python list? Assume that all elements should be set to the same value.

Answer: list comprehension and * operator are fastest followed by while and for loop for loop in list.


# In[ ]:





# In[ ]:


Q3. How do you slice a list to get any other part while missing the rest? (For example, suppose you want to make a new list with the elements first, third, fifth, seventh, and so on.)

Answer:


# In[2]:



b = [1,2,3,4,5,6,7,8,9,10,11,12]
print(b[::2])


# In[ ]:





# In[ ]:


Q4. Explain the distinctions between indexing and slicing.

Answer: “Indexing” means referring to an element of an iterable by its position within the iterable. “Slicing” means getting a subset of elements from an iterable based on their indices.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q5. What happens if one of the slicing expression's indexes is out of range");get_ipython().run_line_magic('pinfo', 'range')

Answer: empty list comes



# In[3]:


b = [1,2,3,4,5,6,7,8,9,10,11,12]
print(b[34:44:1])
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. If you pass a list to a function, and if you want the function to be able to change the values of the list—so that the list is different after the function returns—what action should you avoid');get_ipython().run_line_magic('pinfo', 'avoid')

Answer: the list will change list are mutable but we can also prevent that by creating a deepcopy of it before.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What is the concept of an unbalanced matrix');get_ipython().run_line_magic('pinfo', 'matrix')

Answer: A matrix is balanced if all cells in the matrix are balanced and a cell of the matrix is balanced if the number of cells in that matrix that are adjacent to that cell is strictly greater than the value written in this cell. .

Input: N = 3, M = 3

mat[][] = {{1, 2, 3},

{4, 5, 6},

{7, 8, 9}}

Output: Unbalanced

Explanation: Each cell of the given grid is not stable, so the overall grid is unbalanced.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. Why is it necessary to use either list comprehension or a loop to create arbitrarily large matrices');get_ipython().run_line_magic('pinfo', 'matrices')

Answer: list comprehension or a loop specifically list comprehension can simplify our code, but if you put too much logic inside, they will instead become harder to read and understand. loop specifically are also fast as we have seen in previous questions using time.


# In[ ]:




