#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 6


# In[ ]:





# In[ ]:


Q1. Describe three applications for exception processing.

Answer: Python provides the number of built-in exceptions, but here we are describing the common standard exceptions. A list of common exceptions that can be thrown from a standard Python program is given below.

ZeroDivisionError: Occurs when a number is divided by zero.
NameError: It occurs when a name is not found. It may be local or global.
IndentationError: If incorrect indentation is given.
IOError: It occurs when Input Output operation fails.
EOFError: It occurs when the end of the file is reached, and yet operations are being performed.


# In[ ]:





# In[ ]:



get_ipython().set_next_input("Q2. What happens if you don't do something extra to treat an exception");get_ipython().run_line_magic('pinfo', 'exception')

Answer: When an exception occurred, if you don't handle it, the program terminates abruptly and the code past the line that caused the exception will not get executed. Because of not handling exceptions while deployment of end products users can face issues at their end while using the product.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q3. What are your options for recovering from an exception in your script');get_ipython().run_line_magic('pinfo', 'script')

Answer: Exception handling and logging the exceptions are basic ideas that a programmer should follow. Also writing the code in modular fashion helps in easily fidong the errors in end products and logging make it easier for deelopers to resolve the issue at their end.


# In[ ]:





# In[ ]:


4. Describe two methods for triggering exceptions in your script.

Answer: An unhandled exception displays an error message and the program suddenly crashes. To avoid such a scenario, there are two methods to handle Python exceptions:

Try – This method catches the exceptions raised by the program

Raise – Triggers an exception manually using custom exceptions


# In[ ]:





# In[ ]:


Q5. Identify two methods for specifying actions to be executed at termination time, regardless of whether or not an exception exists.

Answe: These methods are finally and else a simple expmple using them is shown above.


# In[ ]:





# In[ ]:




