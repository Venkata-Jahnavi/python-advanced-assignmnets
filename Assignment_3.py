#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment_3


# In[ ]:





# In[ ]:


get_ipython().set_next_input('What is the concept of an abstract superclass');get_ipython().run_line_magic('pinfo', 'superclass')
Answer: Abstract Super Class. A common superclass for several subclasses. Factor up common behavior. Define the methods they all respond to. Methods that subclasses should implement are declared abstract.



# In[1]:


class test:
    def __init__(self, a , b  , c ,d ) :
        self.__a = a 
        self.b = b
        self.c = c 
        self.d = d 
    def test_custome(self , v ) : 
         return v - self.__a 
    
    def __str__(self):
        return "this is my test code for abstraction"
     


# In[2]:



class test1(test):
    def __init__(self, j , *args):
        super(test1,self).__init__(*args) #
        self.j = j 

m = test1(4,5,6,7,8)
print(m.b)
print(m.c)
print(m.d)
print(m.test_custome(8))
print(m._test__a)


# In[ ]:





# In[ ]:


get_ipython().set_next_input("What happens when a class statement's top level contains a basic assignment statement");get_ipython().run_line_magic('pinfo', 'statement')
Answer: When a class statement's top level contains a basic assignment statement they are considered as class attributes and can be used by functions inside a class or can be called by reating a class object.


# In[3]:


class Dog:
     
    # A simple class attribute
    attr1 = "mammal"
    attr2 = "dog"
 
    # A sample method 
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

Rodger = Dog() # Object instantiation
 
print(Rodger.attr1) # Accessing class attributes and method through objects
Rodger.fun()


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Why does a class need to manually call a superclass's init method");get_ipython().run_line_magic('pinfo', 'method')
Answer: It's because one needs to define something that is NOT done in the base class init , and the only possibility to obtain that is to put its execution in a derived class init function


# In[ ]:


get_ipython().set_next_input('How can you augment, instead of completely replacing, an inherited method');get_ipython().run_line_magic('pinfo', 'method')
Answer: In python to override a method provided by an ancestor class, we have to decide if and when to call its original implementation. This gives the programmer the freedom to decide whether they need to just augment a method or to replace it completely.


# In[4]:


class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

class Rectangle(GraphicalEntity):
    pass

class Square(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, size):
        super().resize(size, size)
     


# In[ ]:





# In[ ]:





# In[ ]:


get_ipython().set_next_input('How is the local scope of a class different from that of a function');get_ipython().run_line_magic('pinfo', 'function')
Answer: Local scope : Local scope is a kind of block scope which are only visible from their point of declaration to the end of the function or lambda body.

Class scope : Names of class members have class scope, which extends throughout the class definition regardless of the point of declaration.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




