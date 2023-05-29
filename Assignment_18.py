#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 18


# In[ ]:





# In[ ]:


Q1. Describe the differences between text and binary files in a single paragraph.

Answer: Binary file contains the data in the form of 0 and 1(series of binary values) and text files contains the data in the form of stream of characters.In general binary files are identified as executable files. But binary files are not in readable form as like text file.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What are some scenarios where using text files will be the better option? When would you like to use binary files instead of text files');get_ipython().run_line_magic('pinfo', 'files')

Answer: text files are commonly used for storage of information. They avoid some of the problems encountered with other file formats, such as endianness, padding bytes, or differences in the number of bytes in a machine word.

Binary files are used to store data more compactly. In the text file, a special character whose ASCII value is 26 inserted after the last character to mark the end of file. In the binary file no such character is present. Files keep track of the end of the file from the number of characters present.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What are some of the issues with using binary operations to read and write a Python integer directly to disc');get_ipython().run_line_magic('pinfo', 'disc')

Answer: its acutally easy to read a write abinary file with rb and wb mode Alternatively we can use open() and close() can be called explicitly. However, this method requires us to perform error handling ourself, that is, ensure that the file is always closed, even if there is an error during writing. So, using the “with” statement is better in this regard as it will automatically close the file when the block ends.


# In[ ]:





# In[ ]:


Q4. Describe a benefit of using the with keyword instead of explicitly opening a file.

Answer: The with statement itself ensures proper acquisition and release of resources. An exception during the file.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. Does Python have the trailing newline while reading a line of text? Does Python append a newline when you write a line of text');get_ipython().run_line_magic('pinfo', 'text')

Answer: Python readline() is a file method that helps to read one complete line from the given file. It has a trailing newline (“\n”) at the end of the string returned. for the second part python uses a backslash escape, \n , which Python converts to a newline character in string literals. It just concatenates your string, name , and that newline character into a bigger string, which gets written to the file.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What file operations enable for random-access operation');get_ipython().run_line_magic('pinfo', 'operation')

Answer: wecan set offsets in file But if we want to access data in a random fashion, then Python gives us seek() and tell() functions to do so.


# In[ ]:





# In[ ]:


get_ipython().set_next_input("Q7. When do you think you'll use the struct package the most");get_ipython().run_line_magic('pinfo', 'most')

Answer: The struct module in Python is used to convert native Python data types such as strings and numbers into a string of bytes and vice versa. What this means is that users can parse binary files of data stored in C structs in Python.

It is used mostly for handling binary data stored in files or from network connections, among other sources.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q8. When is pickling the best option');get_ipython().run_line_magic('pinfo', 'option')

Answer: The Python pickle module is a better choice for all the remaining use cases. If we don't need a human-readable format or a standard interoperable format, or if we need to serialize custom objects, then go with pickle .


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q9. When will it be best to use the shelve package');get_ipython().run_line_magic('pinfo', 'package')

Answer: The shelve module implements persistent storage for arbitrary Python objects which can be pickled, using a dictionary-like API. The shelve module can be used as a simple persistent storage option for Python objects when a relational database is overkill.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q10. What is a special restriction when using the shelve package, as opposed to using other data dictionaries');get_ipython().run_line_magic('pinfo', 'dictionaries')

Answer: The shelf dictionary has certain restrictions. Only string data type can be used as key in this special dictionary object, whereas any picklable Python object can be used as value.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




