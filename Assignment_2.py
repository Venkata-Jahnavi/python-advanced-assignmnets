#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment_2


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the relationship between classes and modules');get_ipython().run_line_magic('pinfo', 'modules')

Answer: Modules are collections of methods and constants. They cannot generate instances. Classes may generate instances (objects), and have per-instance state (instance variables).


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. How do you make instances and classes');get_ipython().run_line_magic('pinfo', 'classes')

Answer: Classes can be cretaed with the help of keyword class. To create instances of a class, we can call the class using class name and pass in whatever arguments its init method accepts.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. Where and how should be class attributes created');get_ipython().run_line_magic('pinfo', 'created')

Answer: Any variable that is bound in a class is a class attribute. Any function defined within a class is a method. Methods receive an instance of the class, conventionally called self, as the first argument. For example


# In[2]:


class MyClass:
    attr1 = 10        #class attributes
    attr2 = "hello"

    def method1(self):
        print( MyClass.attr1)   #reference the class attribute

    def method2(self):
        print( MyClass.attr2)   #reference the class attribute

    def method3(self, text):
        self.text = text        #instance attribute
        print( text, self.text)   #print my argument and my attribute

    method4 = method3   #make an alias for method3
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. Where and how are instance attributes created');get_ipython().run_line_magic('pinfo', 'created')

Answer: Instance attributes are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.


# In[ ]:





# In[ ]:



get_ipython().set_next_input('Q5. What does the term "self" in a Python class mean');get_ipython().run_line_magic('pinfo', 'mean')

Answer: self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. How does a Python class handle operator overloading');get_ipython().run_line_magic('pinfo', 'overloading')

Answer: The operator overloading in Python means provide extended meaning beyond their predefined operational meaning. Such as, we use the "+" operator for adding two integers as well as joining two strings or merging two lists. We can achieve this as the "+" operator is overloaded by the "int" class and "str" class. The user can notice that the same inbuilt operator or function is showing different behaviour for objects of different classes. This process is known as operator overloading. For example:


# In[3]:


class complex_1:  
    def __init__(self, X, Y):  
        self.X = X  
        self.Y = Y  
   
    # Now, we will add the two objects  
    def __add__(self, U):  
        return self.X + U.X, self.Y + U.Y  
   
Object_1 = complex_1(23, 12)  
Object_2 = complex_1(21, 22)  
Object_3 = Object_1 + Object_2  
print (Object_3)  
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. When do you consider allowing operator overloading of your classes');get_ipython().run_line_magic('pinfo', 'classes')

Answer: Suppose that we have two objects which are a physical representation of a class (user-defined data type) and we have to add two objects with binary '+' operator it throws an error, because compiler don't know how to add two objects. So we define a method for an operator and that process is called operator overloading.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. What is the most popular form of operator overloading');get_ipython().run_line_magic('pinfo', 'overloading')

Answer : A very popular and convenient example is the Addition (+) operator. the '+' operator operates on two numbers and the same operator operates on two strings. It performs “Addition” on numbers whereas it performs “Concatenation” on strings.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code');get_ipython().run_line_magic('pinfo', 'code')

Answer: The two most important concepts to grasp in order to comprehend Python OOP code are polymorphism and inheritence.


# In[4]:


#polymorphism example :
class ineuron:
    def msg(self):
        print("this is a msg to ineruon")
          
class xyz:  
    def msg(self):
        print("this is a msg to xyz")     

def test(notes):
    notes.msg()

i = ineuron()
x = xyz()

test(i) # function giving some result
test(x) # same function giving some other result


# In[ ]:





# In[5]:


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





# In[ ]:





# In[ ]:




