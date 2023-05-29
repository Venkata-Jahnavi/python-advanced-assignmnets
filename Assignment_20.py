#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment20


# In[ ]:





# In[ ]:


Q1. Compare and contrast the float and Decimal classes' benefits and drawbacks.

Answer: Float stores an approximate value and decimal stores an exact value. In summary, exact values like money should use decimal, and approximate values like scientific measurements should use float. When multiplying a non integer and dividing by that same number, decimals lose precision while floats do not.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q2. Decimal('1.200') and Decimal('1.2') are two objects to consider. In what sense are these the same object? Are these just two ways of representing the exact same value, or do they correspond to different internal states");get_ipython().run_line_magic('pinfo', 'states')

Answer: the output of both od them will be same this is just a way of representing precision upto 3 decimal points basic mathematics can be seen here in below example. the deciam class while outputting the result rund off the value to 1.2 from 1.200


# In[1]:



c  = 1.200
d = 1.2 
print(c,d)


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q3. What happens if the equality of Decimal('1.200') and Decimal('1.2') is checked");get_ipython().run_line_magic('pinfo', 'checked')

Answer: Float stores an approximate value and decimal stores an exact value


# In[2]:


c  = 1.200
d = 1.2 
if c == d:
  print(c,d)
print(type(c))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. Why is it preferable to start a Decimal object with a string rather than a floating-point value');get_ipython().run_line_magic('pinfo', 'value')

Answer: Because using floats for currency will just cause errors down the road. floats are NOT usable for representing real world values like money - not reliably, anyways.


# In[3]:


from decimal import *
getcontext().prec = 6
print(Decimal(1) / Decimal(7))
getcontext().prec = 28
print(Decimal(1) / Decimal(7))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. In an arithmetic phrase, how simple is it to combine Decimal objects with integers');get_ipython().run_line_magic('pinfo', 'integers')

Answer: Shown below


# In[4]:


.6 + 1


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. Can Decimal objects and floating-point values be combined easily');get_ipython().run_line_magic('pinfo', 'easily')

Answer: Decimal objects cannot generally be combined with floats or instances of fractions.


# In[ ]:





# In[ ]:


Q7. Using the Fraction class but not the Decimal class, give an example of a quantity that can be expressed with absolute precision.


# In[5]:


from fractions import Fraction

print (Fraction(11, 35))
# returns Fraction(11, 35)
print (Fraction(10, 18))
# returns Fraction(5, 9)
print (Fraction())
# returns Fraction(0, 1)


# In[6]:



from fractions import Fraction
print (Fraction('3.14159265358979323846'))
print (Fraction('3.14159265358979323846').limit_denominator(10000))
print (Fraction('3.14159265358979323846').limit_denominator(100))
print (Fraction('3.14159265358979323846').limit_denominator(10))
print (Fraction(125, 50).numerator)
print (Fraction(125, 50).denominator)


# In[ ]:





# In[ ]:


Q8. Describe a quantity that can be accurately expressed by the Decimal or Fraction classes but not by a floating-point value.

Answer: 0.00011 is a finite representation of an infinite number of digits. That doesn't help us with floating-point. Floating-point does not represent numbers using repeat bars; it represents them with a fixed number of bits it can be represented by decimal or fraction class


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9.Consider the following two fraction objects: Fraction(1, 2) and Fraction(1, 2). (5, 10). Is the internal state of these two objects the same? Why do you think that is');get_ipython().run_line_magic('pinfo', 'is')

Answer: the internal state is same will give fraction of 1/2


# In[ ]:





# In[ ]:



get_ipython().set_next_input('Q10. How do the Fraction class and the integer type (int) relate to each other? Containment or inheritance');get_ipython().run_line_magic('pinfo', 'inheritance')

Answer: Inheritence

