#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment_5


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the meaning of multiple inheritance');get_ipython().run_line_magic('pinfo', 'inheritance')

Answer: Multiple inheritance means that a subclass can inherit from two or more superclasses.


# In[2]:



#multiple inheritence
class Ineuron:
    company_website = 'https://ineuron.ai/'
    name = 'iNeuron'
 
    def contact_details(self):
        print('Contact us at ', self.company_website)

class OS:
    multi_task = True
    os_name = 'Windows OS'
    name = "arun"

class windows(OS, Ineuron):
    def __init__(self):
        if self.multi_task is True:
            print('multi_task')
        print('Name: {}'.format(self.name))
 
windows = windows() 


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What is the concept of delegation');get_ipython().run_line_magic('pinfo', 'delegation')

Answer: Answer : Delegation is an object oriented technique (also called a design pattern). Let's say we have an object x and want to change the behaviour of just one of its methods. we can create a new class that provides a new implementation of the method we're interested in changing and delegates all other methods to the corresponding method of x.

Delegation can be imlemented easily. For example, the following class implements a class that behaves like a file but converts all written data to uppercase:


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What is the concept of composition');get_ipython().run_line_magic('pinfo', 'composition')

Answer: It is one of the fundamental concepts of Object-Oriented Programming. In this concept, we describe a class that references to one or more objects of other classes as an Instance variable. Here, by using the class name or by creating the object we can access the members of one class inside another class. It enables creating complex types by combining objects of different classes. It means that a class Composite can contain an object of another class Component. This type of relationship is known as Has-A Relation.

class A : # variables of class A # methods of class A ... ... class B : # by using "obj" we can access member's of class A. obj = A() # variables of class B # methods of class B ... ...


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What are bound methods and how do we use them');get_ipython().run_line_magic('pinfo', 'them')

Answer: A bound method is the one which is dependent on the instance of the class as the first argument. It passes the instance as the first argument which is used to access the variables and functions. In Python 3 and newer versions of python, all functions in the class are by default bound methods.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is the purpose of pseudoprivate attributes');get_ipython().run_line_magic('pinfo', 'attributes')

Answer: Pseudoprivate attributes are useful in larger frameworks or tools, both to avoid introducing new method names that might accidentally hide definitions elsewhere in the class tree and to reduce the chance of internal methods being replaced by names defined lower in the tree.


# In[3]:



class Info:
    def __init__(self):
        self.__name = 'arun'
    def __say(self):
        return self.__name
a = Info()
print(a._Info__name) 
print(a._Info__say()) 
     


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




