#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 14


# In[ ]:





# In[ ]:


Q1. Is an assignment operator like += only for show? Is it possible that it would lead to faster results at the runtime? 
Answer: Yes it is inplace adding


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q2. What is the smallest number of statements you'd have to write in most programming languages to replace the Python expression a, b = a + b, a");get_ipython().run_line_magic('pinfo', 'a')

Answer: a = a+b
b = a


# In[ ]:





# In[ ]:


Q3. In Python, what is the most effective way to set a list of 100 integers to 0?

Answer: list.clear()


# In[ ]:





# In[ ]:


Q4. What is the most effective way to initialise a list of 99 integers that repeats the sequence 1, 2, 3? S If necessary, show step-by-step instructions on how to accomplish this.


# In[1]:



l = []
for i in range(100):
  l.append(i)
  print(i)


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q5. If you're using IDLE to run a Python application, explain how to print a multidimensional list as efficiently");get_ipython().run_line_magic('pinfo', 'efficiently')


# In[2]:



m = 4
n = 5
  
a = [[0 for x in range(n)] for x in range(m)]
print(a)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. Is it possible to use list comprehension with a string? If so, how can you go about doing it');get_ipython().run_line_magic('pinfo', 'it')


# In[3]:



h_letters = [ letter for letter in 'ASHISH' ]
print( h_letters)
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. From the command line, how do you get support with a user-written Python programme? Is this possible from inside IDLE');get_ipython().run_line_magic('pinfo', 'IDLE')

Answeer: we can peform different things like downloading packages cecking python creating environemnt from CLI a terminal window is there in IDLE to do the same.


# In[ ]:





# In[ ]:


Q8. Functions are said to be “first-class objects” in Python but not in most other languages, such as C++ or Java. What can you do in Python with a function (callable object) that you can't do in C or C++?

Answer: functions behave like any other object, such as an int or a list. That means that you can use functions as arguments to other functions, store functions as dictionary values, or return a function from another function. This leads to many powerful ways to use functions.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. How do you distinguish between a wrapper, a wrapped feature, and a decorator');get_ipython().run_line_magic('pinfo', 'decorator')

Answer: Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

@wrapper

def function(n):

statements(s)

similar to

def function(n):

statement(s)

function = wrapper(function)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q10. If a function is a generator function, what does it return');get_ipython().run_line_magic('pinfo', 'return')

Answer: A generator is a special type of function which does not return a single value, instead, it returns an iterator object with a sequence of values. In a generator function, a yield statement is used rather than a return statement.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q11. What is the one improvement that must be made to a function in order for it to become a generator function in the Python language');get_ipython().run_line_magic('pinfo', 'language')

Answer: yield keyword


# In[ ]:





# In[ ]:


Q12. Identify at least one benefit of generators.

Answer: Generator functions allow you to declare a function that behaves like an iterator. They allow programmers to make an iterator in a fast, easy, and clean way.

