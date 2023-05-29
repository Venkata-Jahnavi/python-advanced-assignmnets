#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 09


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. In Python 3.X, what are the names and functions of string object types');get_ipython().run_line_magic('pinfo', 'types')

Answer: There are many string functions some of them are mentioned below isascii(), islower(), isdigit(), upper(), lower(), lstrip(). rstrip()

basically after definign the string we can use (dot) and them tab in jupyter notebook or ctrl+space in colab to access these we don't need to remember them.

I refer this link for help with strings functions https://www.w3schools.com/python/python_ref_string.asp


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. How do the string forms in Python 3.X vary in terms of operations');get_ipython().run_line_magic('pinfo', 'operations')

Answer: The type can be used with format codes just add a % symbol before them :

‘d’ for integers
‘f’ for floating-point numbers
‘b’ for binary numbers
‘o’ for octal numbers
‘x’ for octal hexadecimal numbers
‘s’ for string
‘e’ for floating-point in an exponent format
get_ipython().set_next_input('Q3. In 3.X, how do you put non-ASCII Unicode characters in a string');get_ipython().run_line_magic('pinfo', 'string')

Answer: In order to use non-ASCII characters, Python requires explicit encoding and decoding of strings into Unicode. we can check using the ascii value using ord()


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. In Python 3.X, what are the key differences between text-mode and binary-mode files');get_ipython().run_line_magic('pinfo', 'files')

Answer: The major difference between these two is that a text file contains textual information in the form of alphabets, digits and special characters or symbols. On the other hand, a binary file contains bytes or a compiled version of a text file.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q5. How can you interpret a Unicode text file containing text encoded in a different encoding than your platform's default");get_ipython().run_line_magic('pinfo', 'default')

Answer: we can do it by hit and trieal trying different types of ending like utf-8, utf-16 etc.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What is the best way to make a Unicode text file in a particular encoding format');get_ipython().run_line_magic('pinfo', 'format')


# In[1]:



unicode_text = u'ʑʒʓʔʕʗʘʙʚʛʜʝʞ'
encoded_unicode = unicode_text.encode("utf8")

a_file = open("textfile.txt", "wb")
a_file.write(encoded_unicode)

a_file = open("textfile.txt", "r")#r reads contents of a file

contents = a_file.read()

print(contents)


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. What qualifies ASCII text as a form of Unicode text');get_ipython().run_line_magic('pinfo', 'text')

Answer: The first 128 Unicode code points represent the ASCII characters, which means that any ASCII text is also a UTF-8 text. As long as it contains no code points in the reserved range U+D800–U+DFFF, a UCS-2 text is valid UTF-16 text.

Encoding formats: UTF-8; UTF-16; GB18030;

Standard: Unicode Standard

Alias(es): Universal Coded Character Set (UCS)

