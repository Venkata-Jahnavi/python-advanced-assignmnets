#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 11


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the concept of a metaclass');get_ipython().run_line_magic('pinfo', 'metaclass')

Answer: In object-oriented programming, a metaclass is a class whose instances are classes. Just as an ordinary class defines the behavior of certain objects, a metaclass defines the behavior of certain classes and their instances.

A Class is also an object, and just like any other object, it’s an instance of something called Metaclass. A special class type creates these Class objects. The type class is default metaclass which is responsible for making classes.


# In[1]:


class Student:
	pass
stu_obj = Student()
# Print type of object of Student class
print("Type of stu_obj is:", type(stu_obj))


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q2. What is the best way to declare a class's metaclass");get_ipython().run_line_magic('pinfo', 'metaclass')


# In[2]:


n = 5
d = { 'x' : 1, 'y' : 2 }
class Foo:
     pass
x = Foo()
for obj in (n, d, x):
  print(type(obj) is obj.__class__)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. How do class decorators overlap with metaclasses for handling classes');get_ipython().run_line_magic('pinfo', 'classes')

Answer: Decorators are much, much simpler and more limited and therefore should be preferred whenever the desired effect can be achieved with either a metaclass or a class decorator.

we can do anything with a class decorator, we can of course do with a custom metaclass (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's new or init that make the class object.

The same applies to all magic methods, i.e., to all kinds of operations as applied to the class object itself (as opposed to, ones applied to its instances, which use magic methods as defined in the class operations on the class object itself use magic methods as defined in the metaclass).


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




