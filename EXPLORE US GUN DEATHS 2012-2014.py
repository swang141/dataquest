#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
csvreader = csv.reader(open('guns.csv', 'r'))
data = list(csvreader)
print (data[:5])


# In[3]:


header = data[0]
data = data[1:]
print (header)
print (data[:5])


# In[4]:


years = [row[1] for row in data]


# In[5]:


year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] = 1
print (year_counts)


# In[6]:


import datetime
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
print(dates[:5])
date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] =1
print (date_counts)
    


# In[7]:


'''import datetime
dates = []
for row in data[:3]:
    a = datetime.datetime(year = int(row[1]), month = int(row[2]), day =1)
    print (a)
    dates.append(a)
    print (dates[:5])    '''


# In[8]:


sex = [row[5] for row in data]
sex_count = {}
for s in sex:
    if s in sex_count:
        sex_count[s] += 1
    else:
        sex_count[s] =1
print (sex_count)


# In[9]:


#method 2
sexes = [row[5] for row in data]
sex_counts = {}
for sex in sexes:
    if sex not in sex_counts:
        sex_counts[sex] = 0
    sex_counts[sex] += 1
sex_counts


# In[10]:


races= [row[7] for row in data]
race_counts = {}
for race in races:
    if race not in race_counts:
        race_counts[race] = 0
    race_counts[race] += 1
race_counts


# In[11]:


#  Much more male than female die from gun shot
# White is the largest group who die from gun shot
# can examine intent and examine if there is any correlation between the intent and races/sex/season
# The total amount of populary may influence the percentage of people die from gun shot grouped by races


# In[12]:


census = list(csv.reader(open('census.csv','r')))
print (census)


# In[13]:


mapping={}
mapping['Asian/Pacific Islander'] = int(census[1][census[0].index('Race Alone - Asian')]) + int(census[1][census[0].index('Race Alone - Native Hawaiian and Other Pacific Islander')])
mapping['Black'] = int(census[1][census[0].index('Race Alone - Black or African American')])
mapping['Hispanic'] = int(census[1][census[0].index('Race Alone - Hispanic')])
mapping['Native American/Native Alaskan'] = int(census[1][census[0].index('Race Alone - American Indian and Alaska Native')])
mapping['White'] = int(census[1][census[0].index('Race Alone - White')])
mapping   



# In[14]:


race_per_hundredk = {}
for k,v in race_counts.items():
    race_per_hundredk[k] = v/int(mapping[k])*100000
race_per_hundredk
    


# In[15]:


intents = [row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for index, race in enumerate(races):
    if intents[index] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
homicide_race_counts_per_hundredk = {}
for k,v in homicide_race_counts.items():
    homicide_race_counts_per_hundredk[k] =  v/mapping[k]*100000
homicide_race_counts_per_hundredk 
    


# In[16]:


#Black and Hispanic have largest homicide rate 


# In[17]:


#It appears that gun related homicides in the US disproportionately affect people in the Black and Hispanic racial categories.

#Some areas to investigate further:

#The link between month and homicide rate.
#Homicide rate by gender.
#The rates of other intents by gender and race.
#Gun death rates by location and education.


# In[18]:


homicide_month = {}
for row in data:
    if row[3] == 'Homicide':
         if row[2] not in homicide_month:
            homicide_month[row[2]] = 1
         else:
            homicide_month[row[2]] += 1
homicide_month
    
   


# In[19]:


homicide_gender = {}
for row in data:
    if row[3] == 'Homicide':
        if row[5] not in homicide_gender:
            homicide_gender[row[5]] = 1
        else:
            homicide_gender[row[5]] += 1
homicide_gender_rate={}
for k, v in homicide_gender.items():
    homicide_gender_rate[k] = v/int(census[1][9])*100000
homicide_gender_rate


# In[20]:


def intents_rate(intent):
    intents_by_gender = {}
    genders = [row[5] for row in data]
    for index, race in enumerate (races): 
        intents_by_race = {}
        if intents[index] == intent:
            if genders[index] not in intents_by_gender:
                intents_by_race[race] = 1
                intents_by_gender[genders[index]] = intents_by_race
            else:
                if race not in intents_by_gender[genders[index]]:
                    intents_by_gender[genders[index]][race] = 1
                else:
                    intents_by_gender[genders[index]][race] += 1
    return intents_by_gender
intents_rate('Accidental')              
                       
                       
                    
                        
                
           

                    
                   
            


# In[21]:


# methond 2
def intents_rate(intent):
    intents_by_gender = {}
    genders = [row[5] for row in data]
    for index, race in enumerate (races): 
        if intents[index] == intent:
            if genders[index] not in intents_by_gender:
                intents_by_gender[genders[index]] = {race:1}
            else:
                if race not in intents_by_gender[genders[index]]:
                    intents_by_gender[genders[index]][race] = 1
                else:
                    intents_by_gender[genders[index]][race] += 1
    return intents_by_gender
intents_rate('Accidental')              


# In[25]:


index_total = int(census[0].index('Total'))
total = int(census[1][index_total])
edloc_death = {}
for row in data:
    if row[-1] not in edloc_death:
        edloc_death[row[-1]] = {row[-2]: 1/total*100000}
    else:
        if row[-2] not in edloc_death[row[-1]]:
            edloc_death[row[-1]][row[-2]] = 1/total*100000
        else:
            edloc_death[row[-1]][row[-2]] += 1/total*100000

edloc_death


# In[ ]:





# In[ ]:




