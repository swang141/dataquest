
# coding: utf-8

# In[1]:


import pandas as pd
star_wars = pd.read_csv('star_wars.csv', encoding = 'ISO-8859-1')
star_wars = star_wars[pd.notnull(star_wars['RespondentID'])]
star_wars.head()


# In[2]:


yes_no = {'Yes': True, 'No': False}
star_wars['Have you seen any of the 6 films in the Star Wars franchise?'].map(yes_no)


# In[3]:


star_wars = star_wars.rename(columns = {star_wars.columns[3]:'seen_1', star_wars.columns[4]:'seen_2',star_wars.columns[5]:'seen_3',star_wars.columns[6]:'seen_4',star_wars.columns[7]:'seen_5',star_wars.columns[8]:'seen_6'})
star_wars


# In[4]:


import numpy as np
seen_mapping = {
    "Star Wars: Episode I  The Phantom Menace": True,
    np.nan: False,
    "Star Wars: Episode II  Attack of the Clones": True,
    "Star Wars: Episode III  Revenge of the Sith": True,
    "Star Wars: Episode IV  A New Hope": True,
    "Star Wars: Episode V The Empire Strikes Back": True,
    "Star Wars: Episode VI Return of the Jedi": True
}

for col in star_wars.columns[3:9]:
    star_wars[col] = star_wars[col].map(seen_mapping)
star_wars[star_wars.columns[3:9]]


# In[5]:


star_wars[star_wars.columns[9:15]] = star_wars[star_wars.columns[9:15]].astype(float)
star_wars = star_wars.rename(columns = {star_wars.columns[9]:'rankingg_1', star_wars.columns[10]:'rankingg_2', star_wars.columns[11]:'rankingg_3', star_wars.columns[12]:'rankingg_4', star_wars.columns[13]:'rankingg_5', star_wars.columns[14]:'rankingg_6'})
print(star_wars[star_wars.columns[9:15]])


# In[6]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
rank = star_wars[star_wars.columns[9:15]].mean()
rank.plot.bar()
plt.show()


# In[7]:


#episode 5 is the most popular one, while episode 3 is the least popular one


# In[8]:


count = star_wars[star_wars.columns[3:9]].sum()
count.plot.bar()
plt.show()


# In[9]:


#Most people have watched episode 5, while least people have watched episode 3. The result matches the ranking result. 


# In[10]:


from numpy import arange
males = star_wars[star_wars['Gender'] == 'Male']
females = star_wars[star_wars['Gender'] == 'Female']
male_ranks = males[males.columns[9:15]].mean()
female_ranks = females[females.columns[9:15]].mean()

fig, ax = plt.subplots()
bar_male = ax.bar(left=arange(6)+0.2, height=male_ranks, width = 0.2, color='red', align='center')
bar_female = ax.bar(left=arange(6)+0.4, height = female_ranks, width = 0.2, align='center')
ax.legend((bar_male, bar_female),('male', 'female'))
ax.set_xticks(arange(6)+0.3)
ax.set_xticklabels(star_wars.columns[9:15], rotation = 90)



# In[11]:


male_seen = males[males.columns[3:9]].sum()
female_seen = females[females.columns[3:9]].sum()

fig, ax = plt.subplots()
bar_male = ax.bar(left=arange(6)+0.2, height=male_seen, width = 0.2, color='red', align='center')
bar_female = ax.bar(left=arange(6)+0.4, height = female_seen, width = 0.2, align='center')
ax.legend((bar_male, bar_female),('male', 'female'), loc='upper right', bbox_to_anchor = (1.3, 1))
ax.set_xticks(arange(6)+0.3)
ax.set_xticklabels(star_wars.columns[3:9], rotation = 90)


