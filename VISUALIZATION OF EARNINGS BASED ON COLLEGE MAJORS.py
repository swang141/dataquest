#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')


# In[2]:


recent_grads = pd.read_csv('recent-grads.csv')
print(recent_grads.iloc[0, :])
print(recent_grads.describe())


# In[3]:


print(recent_grads.head())
print(recent_grads.tail())


# In[4]:


raw_data_count = recent_grads.shape[0]
print(raw_data_count)


# In[5]:


recent_grads1= recent_grads.dropna()
cleaned_data_count = recent_grads1.shape[0]
print(cleaned_data_count)


# In[6]:


recent_grads.plot(x='Sample_size', y='Median', kind='scatter', title='sample size vs median')
recent_grads.plot(x='Sample_size', y='Unemployment_rate',kind='scatter', title='sample size vs unemployement_rate')
recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Full time vs median')
recent_grads.plot(x='ShareWomen', y='Unemployment_rate',kind='scatter', title='Sharewomen vs unemployement rate')
recent_grads.plot(x='Men', y='Median', kind='scatter', title='men vs median')
recent_grads.plot(x='Women', y='Median', kind='scatter', title='Women vs median')


# In[7]:


#student in less popular majors make more money
#students in subjects that were majority female don't make more money
# less full-time employees major has higher median salary


# In[8]:


col=['Sample_size', 'Median', 'Employed','Full_time', 'ShareWomen', 'Unemployment_rate', 'Men', 'Women']
recent_grads['Sample_size'].hist(bins=25, range=(0,2000))


# In[9]:


recent_grads['Median'].hist(bins=25, range=(0,2000))


# In[10]:


recent_grads['Employed'].hist(bins=25, range=(0,2000))


# In[ ]:





# In[ ]:





# In[11]:


from pandas.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize = (10,10))


# In[12]:


scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))


# In[13]:


recent_grads.loc[:10]['ShareWomen'].plot(kind = 'bar')


# In[ ]:





# In[14]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen', legend= False)


# In[15]:


recent_grads[-10:].plot.bar(x = 'Major', y='Unemployment_rate',legend= False)


# In[16]:


recent_grads[:10].plot.bar(x='Major', y=['Men','Women'])


# In[21]:


recent_grads['Median'].plot.box()


# In[ ]:





# In[22]:


recent_grads['Unemployment_rate'].plot.box()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




