#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 08


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What are the two latest user-defined exception constraints in Python 3.X');get_ipython().run_line_magic('pinfo', 'X')

Answer: Python also provides an exception handling method with the help of try-except. Some of the standard exceptions which are most frequent include IndexError, ImportError, IOError, ZeroDivisionError, TypeError, and FileNotFoundError.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. How are class-based exceptions that have been raised matched to handlers');get_ipython().run_line_magic('pinfo', 'handlers')

Answer: A class-based exception can either cancel the current context or allow for a resume. Exceptions are raised using the statement RAISE EXCEPTION and handled using CATCH in a TRY control structure. Class-based exceptions can be raised in any procedures and can be further propagated by any procedures. A common class based and user defined exception in a single program as shown in preious assignments can be division by zero.


# In[ ]:





# In[ ]:


Q3. Describe two methods for attaching context information to exception artefacts.

Answer: IMPLICIT EXCEPTION CHAINING AND EXPLICIT EXCEPTION CHAINING can be done for attaching context information to exception artefacts.

PEP proposes three standard attributes on exception instances: the context attribute for implicitly chained exceptions, the cause attribute for explicitly chained exceptions, and the traceback attribute for the traceback. A new raise ... from statement sets the cause attribute. An example to illustrate the context attribute():


# In[ ]:





# In[ ]:


Q4. Describe two methods for specifying the text of an exception object's error message.

Answer: try, except, else and finally in else and finally even in except we can add another try except blockto raise an exception that might still come. Basically, we can raise an excepion using the ecept block or using raise command.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. Why do you no longer use string-based exceptions');get_ipython().run_line_magic('pinfo', 'exceptions')

Answer: Accordig to recent updates the standard exceptions are Python classes, and a few new standard exceptions have been added. The obsolete AccessError exception has been deleted. Because it is possible (although unlikely) that this change broke existing code, the Python interpreter can be invoked the command line option -X to disable this feature, and use string exceptions like before. This option is a temporary measure - eventually the string-based standard exceptions will be removed from the language altogether. It hasn't been decided whether user-defined string exceptions will be allowed in Python 2.0.


# In[ ]:





# In[ ]:





# In[ ]:




