#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Is Fandango Still Inflating Ratings?


# In[2]:


#In October 2015, Walt Hickey from FiveThirtyEight published a popular article where he presented strong evidence which suggest that Fandango's movie rating system was biased and dishonest. whether there's any difference between Fandango's ratings for popular movies in 2015 and Fandango's ratings for popular movies in 2016. 


# In[3]:


import pandas as pd
old = pd.read_csv('fandango_score_comparison.csv')
new = pd.read_csv('movie_ratings_16_17.csv')


# In[4]:


old_fandango = old[['FILM', 'Fandango_Stars', 'Fandango_Ratingvalue', 'Fandango_votes', 'Fandango_Difference']]
old_fandango


# In[5]:


new_fandango = new[[ 'movie', 'year', 'fandango']]


# In[6]:


old_fandango


# In[7]:


new_fan_2016 = new_fandango[new_fandango['year'] == 2016]
new_fan_2016


# In[8]:


old_fan_2015 = old_fandango[old_fandango['FILM'].str.contains('(2015)', regex = False) == True]
old_fan_2015


# In[9]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')
plt.style.use('fivethirtyeight')
old_fan_2015['Fandango_Stars'].plot.kde(label = '2015', legend = True)
new_fan_2016['fandango'].plot.kde(label ='2016', legend = True)
plt.xlabel('Ratings')
plt.title ('Fandago Rating Comparison', fontsize = 20)
plt.xlim(0,5)
plt.xticks(np.arange(0,5.5, 0.5))


# In[10]:


#The kernel density shape is left skewed, which means the movie ratings in both years are high. 2016's rating is slightly lower than 2015. 


# In[14]:


old_fan_2015['Fandango_Stars'].value_counts(normalize = True).sort_index()*100


# In[15]:


new_fan_2016['fandango'].value_counts(normalize = True).sort_index()*100


# In[16]:


#From the above two percentile tables, we can see that the percentage of the lower rating (<=3) has been increased, and the loest rating is 2.5 in 2016, compared to 3 in 2015. There is an increased percentage for rating 3.5-4. The percentage for rating 4.5-5 has decreased.  


# In[17]:


mean2015 = old_fan_2015['Fandango_Stars'].mean()
median2015 = old_fan_2015['Fandango_Stars'].median()
mode2015 = old_fan_2015['Fandango_Stars'].mode()
print('2015_mean: {}, 2015_median: {}, 2015_mode: {}'.format(mean2015,median2015,mode2015))


# In[18]:


mean2016 = new_fan_2016['fandango'].mean()
median2016 = new_fan_2016['fandango'].median()
mode2016 = new_fan_2016['fandango'].mode()
print('2016_mean: {}, 2016_median: {}, 2016_mode: {}'.format(mean2016,median2016,mode2016))


# In[42]:


plt.figure(figsize = (12,8) )
plt.bar(np.arange(3)+0.1, (mean2015, median2015, mode2015[0]), width = 0.3, label = '2015')
plt.bar(np.arange(3)+0.2, (mean2016, median2016, mode2016[0]), width = 0.3 , label = '2016', color ='r')
plt.xticks(np.arange(3)+0.25, ('mean', 'median', 'mode'), fontsize = 18)
plt.ylim(0,5)
plt.ylabel('Stars')
plt.xlabel('statistics')
plt.title('Comparing Summary Statistics: 2015 vs 2016', fontsize = 25)
plt.legend(loc='upper center')


# In[54]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




