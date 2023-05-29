#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignmnet-21


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is a probability distribution, exactly? If the values are meant to be random, how can you predict them at all');get_ipython().run_line_magic('pinfo', 'all')

Answer: A probability distribution is a statistical function that describes all the possible values and likelihoods that a random variable can take within a given range. These factors include the distribution's mean (average), standard deviation, skewness, and kurtosis.

If the values are meant to be random, we can predict them using following steps:

Step 1: List all simple events in sample space.

Step 2: Find probability for each simple event.

Step 3: List possible values for random variable X and identify the value for each simple event.

Step 4: Find all simple events for which X = k, for each possible value k.


# In[ ]:





# In[ ]:


Q2. Is there a distinction between true random numbers and pseudo-random numbers, if there is one? Why are the latter considered “good enough”?

Answer: The difference between true random number generators(TRNGs) and pseudo-random number generators(PRNGs) is that TRNGs use an unpredictable physical means to generate numbers (like atmospheric noise), and PRNGs use mathematical algorithms (completely computer-generated). pseudo-random number are good enough because we usually don't need true randomness for most applications. What We need is unpredictability. If we're using a random number generator in a game, we don't care if the numbers are truly random; we only care that they aren't predictable.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What are the two main factors that influence the behaviour of a "normal" probability distribution');get_ipython().run_line_magic('pinfo', 'distribution')

Answer: The first rule states that the sum of the probabilities must equal 1. The second rule states that each probability must be between 0 and 1, inclusive.


# In[ ]:





# In[ ]:


Q4. Provide a real-life example of a normal distribution.

Answer: Rolling A Dice

A fair rolling of dice is also a good example of normal distribution. In an experiment, it has been found that when a dice is rolled 100 times, chances to get '1' are 15-18% and if we roll the dice 1000 times, the chances to get '1' is, again, the same, which averages to 16.7% (1/6).


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. In the short term, how can you expect a probability distribution to behave? What do you think will happen as the number of trials grows');get_ipython().run_line_magic('pinfo', 'grows')

Answer: Depends on the data for the distribution. it initially wil be rising and after a certain threshold achieving it it will go down.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What kind of object can be shuffled by using random.shuffle');get_ipython().run_line_magic('pinfo', 'random.shuffle')

Answer: random provides shuffle() that shuffles the original list in place, and sample() that returns a new list that is randomly shuffled. sample() can also be used for strings and tuples.


# In[ ]:





# In[ ]:


Q7. Describe the math package's general categories of functions.

Answer: sin, cos, sqrt, pow, log, exp etc.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. What is the relationship between exponentiation and logarithms');get_ipython().run_line_magic('pinfo', 'logarithms')

Answer: Logarithmic functions are the inverses of exponential functions. The inverse of the exponential function y = a^x is x = a^y. The logarithmic function y = log_a^x is defined to be equivalent to the exponential equation x = a^y.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. What are the three logarithmic functions that Python supports');get_ipython().run_line_magic('pinfo', 'supports')

Answer: log2(x)

log(x, Base)

log10(x)

log1p(x)Q4

