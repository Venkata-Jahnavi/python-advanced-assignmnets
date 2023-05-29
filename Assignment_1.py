#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment -1


# In[ ]:


get_ipython().set_next_input("Q1. What is the purpose of Python's OOP");get_ipython().run_line_magic('pinfo', 'OOP')

Answer: In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. Where does an inheritance search look for an attribute');get_ipython().run_line_magic('pinfo', 'attribute')

Answer: The inheritance search is simply a search of the tree from bottom to top looking for the lowest occurrence of an attribute name


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. How do you distinguish between a class object and an instance object');get_ipython().run_line_magic('pinfo', 'object')

Answer: Class Object:

An Object is an instance of a Class. A class is like a blueprint while an instance is a copy of the class with actual values. It’s not an idea anymore, it’s an actual dog, like a dog of breed pug who’s seven years old. You can have many dogs to create many different instances, but without the class as a guide, you would be lost, not knowing what information is required.

An object consists of :

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
Instance object:

To create instances of a class, you call the class using class name and pass in whatever arguments its init method accepts.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is the purpose of the init method');get_ipython().run_line_magic('pinfo', 'method')

Answer: The init function is called every time an object is created from a class. The init method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is the purpose of the init method');get_ipython().run_line_magic('pinfo', 'method')

Answer: The init function is called every time an object is created from a class. The init method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What is the process for creating a class instance');get_ipython().run_line_magic('pinfo', 'instance')

Answer: Define a class first then create the functions after the class is made then create the object for calling the functions as per requirements. Example:


# In[2]:


class C:
    def __init__(self, data):
        self.data = data

an_instance = C("abc")
print(an_instance.data)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What is the process for creating a class');get_ipython().run_line_magic('pinfo', 'class')

Answer: A Class is like an object constructor, or a "blueprint" for creating objects. Exxample:


# In[3]:


class MyClass: #create class using class keyword
  x = 5

p1 = MyClass()
print(p1.x)
     


# In[ ]:





# In[ ]:


5
get_ipython().set_next_input('Q8. How would you define the superclasses of a class');get_ipython().run_line_magic('pinfo', 'class')

Answer: The class from which a class inherits is called the parent or superclass. A class which inherits from a superclass is called a subclass, also called heir class or child class. Superclasses are sometimes called ancestors as well.

