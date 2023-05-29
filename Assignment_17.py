#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 17


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. Explain the difference between greedy and non-greedy syntax with visual terms in as few words as possible. What is the bare minimum effort required to transform a greedy pattern into a non-greedy one? What characters or characters can you introduce or change');get_ipython().run_line_magic('pinfo', 'change')

Answer: So the difference between the greedy and the non-greedy match is the following: The greedy match will try to match as many repetitions of the quantified pattern as possible. The non-greedy match will try to match as few repetitions of the quantified pattern as possible.

the bare minimum effort required to transform a greedy pattern into a non-greedy one can be just implemented by using a singlle character. The ? operand makes match non-greedy. E.g. .* is greedy while .*? isn't.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q2. When exactly does greedy versus non-greedy make a difference?  What if you're looking for a non-greedy match but the only one available is greedy");get_ipython().run_line_magic('pinfo', 'greedy')

Answer: So the difference between the greedy and the non-greedy match is the following: The greedy match will try to match as many repetitions of the quantified pattern as possible. The non-greedy match will try to match as few repetitions of the quantified pattern as possible.

example: To make the quantifier non-greedy you simply follow it with a '?' the first 3 characters and then the following 'ab' is matched. greedy by appending a '?' symbol to them: *?, +?, ??, {n,m}?, and {n,}?.

if we're looking for a non-greedy match but the only one available is greedy that will result in matching the shortest possible string.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. In a simple match of a string, which looks only for one match and does not do any replacement, is the use of a nontagged group likely to make any practical difference');get_ipython().run_line_magic('pinfo', 'difference')

Answer: Yes it might do.


# In[ ]:





# In[ ]:


Q4. Describe a scenario in which using a nontagged category would have a significant impact on the program's outcomes.


# In[1]:



import re
 
# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
 
# \d+ will match a group on [0-9], group of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

#a simple + operator can make a huge difference in outcome in case of regular expressions


# In[ ]:





# In[ ]:


Q5. Unlike a normal regex pattern, a look-ahead condition does not consume the characters it examines. Describe a situation in which this could make a difference in the results of your programme.

Answer: While the order of lookaheads doesn't matter on a logical level, we should keep in mind that it may matter for matching speed. If one lookahead is more likely to fail than the other two, it makes little sense to place it in third position and expend a lot of energy checking the first two conditions. Make it first, so that if we're going to fail, we fail early—an application of the design to fail principle from the regex style guide.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. In standard expressions, what is the difference between positive look-ahead and negative look- ahead');get_ipython().run_line_magic('pinfo', 'ahead')

Answer: Positive lookahead: (?= «pattern») matches if pattern matches what comes after the current location in the input string.

Negative lookahead: (?! «pattern») matches if pattern does not match what comes after the current location in the input string.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What is the benefit of referring to groups by name rather than by number in a standard expression');get_ipython().run_line_magic('pinfo', 'expression')

Answer: The advantage to named groups is that it adds readability and understandability to the code, so that we can easily see what part of a regular expression match is being referenced.


# In[ ]:





# In[ ]:


Q8. Can you identify repeated items within a target string using named groups, as in "The cow jumped over the moon"?

Answer: In this particular scenario it may be possible by checking it wu=ith the + tag in regex go check for one or more occurances.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. When parsing a string, what is at least one thing that the Scanner interface does for you that the re.findall feature does not');get_ipython().run_line_magic('pinfo', 'not')

Answer: search() method is able to find a pattern from any position of the string. The re. It searches from start or end of the given string. If we use method findall to search for a pattern in a given string it will return all occurrences of the pattern.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q10. Does a scanner object have to be named scanner');get_ipython().run_line_magic('pinfo', 'scanner')

Answer: The scan module is part of the microscopy package. It provides a framework for multidimensional scanning routines while acquiring data. Not madatory to keep the same name.


# In[ ]:




