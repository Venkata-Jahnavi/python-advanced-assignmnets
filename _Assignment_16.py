#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 16


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the benefit of regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')

Answer: A regular expression is a special sequence of characters that helps us to match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world. The Python module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.


# In[ ]:





# In[ ]:


Q2. Describe the difference between the effects of "(ab)c+" and "a(bc)+." Which of these, if any, is the unqualified pattern "abc+"?

Answer: the result of both of them will be basically computed using the BOADMAS rule according to mathematics so results will be different in both case. taking in terms of regular espressions it causes the resulting RE to match 1 or more repetitions of the preceding RE. (ab)c+ will match ‘ab’ followed by any non-zero number of ‘c’s; it will not match just ‘ab’. similarly for a(bc)+ it will match ‘a’ followed by any non-zero number of ‘bc’s; it will not match just ‘a’.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. How much do you need to use the following sentence while using regular expressions');get_ipython().run_line_magic('pinfo', 'expressions')

import re

Answer: it's a basic import statement to use regular expressions in python


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. Which characters have special significance in square brackets when expressing a range, and under what circumstances');get_ipython().run_line_magic('pinfo', 'circumstances')

Answer: Square brackets ([ ]) designate a character class and match a single character in the string. Inside a character class, only the character class metacharacters (backslash, circumflex anchor and hyphen) have special meaning.

we must use a backslash when we use character class metacharacters as literals inside a character class only. Square brackets that are used as literals must always be escaped with backslash, both inside and outside a character class.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. How does compiling a regular-expression object benefit you');get_ipython().run_line_magic('pinfo', 'you')

Answer: We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search a pattern again without rewriting it.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What are some examples of how to use the match object returned by re.match and re.search');get_ipython().run_line_magic('pinfo', 're.search')

Answer:


# In[1]:


# import re module
import re
Substring ='string'
String1 ='''We are learning regex with geeksforgeeks
		regex is very useful for string matching.
		It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks
		regex is very useful for string matching.
		It is fast too.'''
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What is the difference between using a vertical bar (|) as an alteration and using square brackets as a character set');get_ipython().run_line_magic('pinfo', 'set')

Answer: The vertical bar is a regex "or" means "a or b"

Square brackets are a character class meaning "any character from a or b.

Character class is a shorthand for "or". From this explanation

If we want to match an a or an e use [ae]

A character class matches only a single character.

we can also use hyphen to specify a range such as [0-9] or [a-e]


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. In regular-expression search patterns, why is it necessary to use the raw-string indicator (r)? In replacement strings');get_ipython().run_line_magic('pinfo', 'strings')

Answer: "Regular expressions use the backslash character ('') to indicate special forms or to allow special characters to be used without invoking their special meaning. This collides with Python’s usage of the same character for the same purpose in string literals"

If we want a Python regular expression object which matches a newline character, then we need a 2-character string, consisting of the backslash character followed by the n character. The following lines of code all set prog to a regular expression object which recognises a newline character:

prog = re.compile("\n")

prog = re.compile(r"\n")

