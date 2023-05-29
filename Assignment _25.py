#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Assignment 25


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q1. What is the distinction between a numpy array and a pandas data frame? Is there a way to convert between the two if there is');get_ipython().run_line_magic('pinfo', 'is')

Answer: The Pandas module mainly works with the tabular data, whereas the NumPy module works with the numerical data. NumPy library provides objects for multi-dimensional arrays, whereas Pandas is capable of offering an in-memory 2d table object called DataFrame. NumPy consumes less memory as compared to Pandas.


# In[1]:


import pandas as pd
import numpy as np

data = {'Age': [15,25,35,45],
        'Birth Year': [2006,1996,1986, np.NaN]
        }

df = pd.DataFrame(data, columns = ['Age','Birth Year'])

numpy_array = df.to_numpy()

print(numpy_array)

print(type(numpy_array))
     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q2. What can go wrong when an user enters in a stock-ticker symbol, and how do you handle it');get_ipython().run_line_magic('pinfo', 'it')

Answer: Ticker symbols aren't static and can change in the event of a merger, name change, or delisting. we can implement a try except else and finally block to deal with it.


# In[ ]:





# In[ ]:


Q3. Identify some of the plotting techniques that are used to produce a stock-market chart.

Answer: The main chart types used by most traders are the Line Chart, Candlestick Chart, Renko Chart, and Point and Figure charts. Usingm atplotlib we can make charts.


# In[2]:


import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x*2

# first plot with X and Y data
plt.plot(x, y)

x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]

# second plot with x1 and y1 data
plt.plot(x1, y1, '-.')

plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')
plt.show()

     


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q4. Why is it essential to print a legend on a stock market chart');get_ipython().run_line_magic('pinfo', 'chart')

Answer: legend helps end user to identify the growth of a particular stock by seeing a chart. its crucial in data analytics.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q5. What is the best way to limit the length of a pandas data frame to less than a year');get_ipython().run_line_magic('pinfo', 'year')

Answer: truncate() function is used to truncate a Series or DataFrame before and after some index value. This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q6. What is the definition of a 180-day moving average');get_ipython().run_line_magic('pinfo', 'average')

Answer: a moving average is an indicator that shows the average value of a stock's price over a period (i.e. 10 days, 50 days, 180 days, 200 days, etc) and is usually plotted along with the closing price.


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Q7. Did the chapter\'s final example use "indirect" importing? If so, how exactly do you do it');get_ipython().run_line_magic('pinfo', 'it')

Answer: I didn't get the questioon which importing it is talking bout.


# In[ ]:




