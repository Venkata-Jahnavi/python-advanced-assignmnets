#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 19


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. Define the relationship between a class and its instances. Is it a one-to-one or a one-to-many partnership, for example');get_ipython().run_line_magic('pinfo', 'example')

Answer: A class is a blueprint which you use to create objects. An object is an instance of a class - it's a concrete 'thing' that you made using a specific class. So, 'object' and 'instance' are the same thing, but the word 'instance' indicates the relationship of an object to its class. a single object of a class can access multille functions defiend in the class in form of ine to many relationships.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What kind of data is held only in an instance');get_ipython().run_line_magic('pinfo', 'instance')

Answer: If the value of a variable varies from object to object, then such variables are called instance variables. For every object, a separate copy of the instance variable will be created. Instance variables are not shared by objects.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What kind of knowledge is stored in a class');get_ipython().run_line_magic('pinfo', 'class')

Answer: A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. What exactly is a method, and how is it different from a regular function');get_ipython().run_line_magic('pinfo', 'function')

Answer: Methods are associated with the objects of the class they belong to. Functions are not associated with any object. Functions operate on the data we pass to them as arguments. Methods are dependent on the class they belong to.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. Is inheritance supported in Python, and if so, what is the syntax');get_ipython().run_line_magic('pinfo', 'syntax')

Answer: YES.


# In[1]:


class Ineuron:
    company_website = 'https://ineuron.ai/'
    name = 'iNeuron'
 
    def contact_details(self):
        print('Contact us at ', self.company_website)
 
 
class Datascience(Ineuron):
    def __init__(self):
        self.year_of_establishment= 2018
 
    def est_details(self):
        print('{0} Company was established in {1}'
              .format(self.name,self.year_of_establishment))
 
 
ds = Datascience()
ds.est_details()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. How much encapsulation (making instance or class variables private) does Python support');get_ipython().run_line_magic('pinfo', 'support')

Answer: We can protect variables in the class by marking them private. To define a private variable we can add two underscores as a prefix at the start of a variable name. Private members are accessible only within the class, and we can't access them directly from the class objects.


# In[ ]:





# In[ ]:



get_ipython().set_next_input('Q7. How do you distinguish between a class variable and an instance variable');get_ipython().run_line_magic('pinfo', 'variable')

Answer: Class varibale: It usually maintains a single shared value for all instances of class even if no instance object of the class exists.

Instance Variable: It usually reserves memory for data that the class needs.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q8. When, if ever, can self be included in a class's method definitions");get_ipython().run_line_magic('pinfo', 'definitions')

Answer: Self is always pointing to Current Object.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. What is the difference between the _ add _ and the _ radd _ methods');get_ipython().run_line_magic('pinfo', 'methods')

Answer:


# In[2]:


class Commuter1:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other


    def __radd__(self, other):
        print('radd', self.val, other)
        return other + self.val


x = Commuter1(88)
y = Commuter1(99)

print(x + y)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q10. When is it necessary to use a reflection method? When do you not need it, even though you support the operation in question');get_ipython().run_line_magic('pinfo', 'question')

Answer: Reflection refers to the ability for code to be able to examine attributes about objects that might be passed as parameters to a function. For example, if we write type(obj) then Python will return an object which represents the type of obj. we need it to reflect the behaviour of data being holded.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q11. What is the _ iadd _ method called');get_ipython().run_line_magic('pinfo', 'called')

Answer: So the main difference between add and iadd is that iadd is actually storing that value its adding into the self.value.


# In[3]:


class NumString:

    def __init__(self, value):
        self.value = str(value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

some_num1 = NumString(0) # Create an instance of NumString with 0 as value.
print(str(some_num1)) # Check what is contained within self.value in this instance.

some_num1 + 1 # We add some_num1 to 1, this returns back the calculation using the __add__ method
print(str(some_num1)) # check what some_num1 is holding for a self.value

some_num1 += 2 # We in-place add some_num1 to 2, this stores and returns the new stored value using __iadd__ method.
print(str(some_num1)) # check what some_num1 is holding now?


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q12. Is the _ init _ method inherited by subclasses? What do you do if you need to customize its behavior within a subclass');get_ipython().run_line_magic('pinfo', 'subclass')

Answer: In Python, it is not compulsory that parent class constructor will always be called first. The order in which the init method is called for a parent or a child class can be modified.

A subclass can do more than that; it can define a method that has exactly the same method signature (name and argument types) as a method in its superclass. In that case, the method in the subclass overrides the method in the superclass and effectively replaces its implementation.

