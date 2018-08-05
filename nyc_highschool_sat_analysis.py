
# coding: utf-8

# # Read in the data

# In[135]:


import pandas as pd
import numpy
import re

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}

for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    data[f.replace(".csv", "")] = d


# # Read in the surveys

# In[136]:


all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding='windows-1252')
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding='windows-1252')
survey = pd.concat([all_survey, d75_survey], axis=0)

survey["DBN"] = survey["dbn"]

survey_fields = [
    "DBN", 
    "rr_s", 
    "rr_t", 
    "rr_p", 
    "N_s", 
    "N_t", 
    "N_p", 
    "saf_p_11", 
    "com_p_11", 
    "eng_p_11", 
    "aca_p_11", 
    "saf_t_11", 
    "com_t_11", 
    "eng_t_11", 
    "aca_t_11", 
    "saf_s_11", 
    "com_s_11", 
    "eng_s_11", 
    "aca_s_11", 
    "saf_tot_11", 
    "com_tot_11", 
    "eng_tot_11", 
    "aca_tot_11",
]
survey = survey.loc[:,survey_fields]
data["survey"] = survey


# # Add DBN columns

# In[137]:


data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return "0" + string_representation
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]


# # Convert columns to numeric

# In[138]:


cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]

def find_lat(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

def find_lon(loc):
    coords = re.findall("\(.+, .+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")


# # Condense datasets

# In[139]:


class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]

class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]


# # Convert AP scores to numeric

# In[140]:


cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")


# # Combine the datasets

# In[141]:


combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], on="DBN", how="left")
combined = combined.merge(data["graduation"], on="DBN", how="left")

to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)


# # Add a school district column for mapping

# In[142]:


def get_first_two_chars(dbn):
    return dbn[0:2]

combined["school_dist"] = combined["DBN"].apply(get_first_two_chars)


# # Find correlations

# In[143]:


correlations = combined.corr()
correlations = correlations["sat_score"]
print(correlations)


# # Plotting survey correlations

# In[144]:


# Remove DBN since it's a unique identifier, not a useful numerical value for correlation.
survey_fields.remove("DBN")


# In[120]:


get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
from numpy import arange
cor_sat_score = combined.corr(method='pearson')['sat_score'][survey_fields]
left=arange(len(survey_fields))+0.75
height = cor_sat_score[survey_fields].values
plt.bar(left,height,0.5)
plt.ylabel('sat_score')
plt.xlabel('survey_fileds')
plt.xticks(arange(len(survey_fields))+1, survey_fields, rotation=90)
plt.show()


# In[121]:


#N_s: number of students respond  N_t:number of eligibel teachers, N_p:number of parents respond, saf_t_11:safety and respect score based on teacher respond, aca_s_11:academic score expecation based on student response, saf_tot_11:saftey and respect total score are all correlated with SAT scores.


# In[122]:


combined.plot.scatter('saf_s_11', 'sat_score')


# In[145]:


import numpy as np
from mpl_toolkits.basemap import Basemap 
district = combined.groupby('school_dist').agg(np.mean)

m = Basemap(
    projection='merc', 
    llcrnrlat=40.496044, 
    urcrnrlat=40.915256, 
    llcrnrlon=-74.255735, 
    urcrnrlon=-73.700272,
    resolution='i')
m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)
m.fillcontinents(lake_color='aqua')

longtitudes = district['lon'].tolist()
latitudes = district['lat'].tolist()
m.scatter(longtitudes, latitudes, latlon=True, s=50, zorder=2, c=district['saf_s_11'], cmap='summer')
plt.show()

print(combined['hispanic_per'])


# In[146]:


#lower brooklyn, and some parts of Queens has high safety scores. Upper Brooklyn, Bronx and some parts of Queens have low safety scores. 


# In[147]:


# two scores are generally positively correlated, but not strong. some schools with extremely high saftey scores have mdium sat scores. some schools with highest sat shcool have medium-high safety scores. Generally, schools with low saftey schools have low sat scores. 


# In[148]:


race=['white_per','asian_per','black_per', 'hispanic_per']
race_sat = combined.corr(method = 'pearson')['sat_score'][race]
race_sat.plot.bar()


# In[149]:


#black and hispanic percentage has negative correlation, while white an asian percentags have strong positive correlation.


# In[150]:


combined.plot.scatter('hispanic_per','sat_score')
plt.show()
#hispanic percentage has negative correlation with sat scores.


# In[153]:


print(combined[combined['hispanic_per']>95]['SCHOOL NAME'])


# In[160]:


#most of them are international schools for immigrants.


# In[162]:


combined[combined['hispanic_per']<10][combined['sat_score']>1800].loc[:,['SCHOOL NAME','sat_score']]


# In[167]:


#these are very well-known high shcools that require school entrance exams and only admit best students


# In[177]:


sex_cor = combined.corr(method='pearson').loc[['male_per','female_per'],'sat_score']
sex_cor.plot.bar()


# In[179]:


#male percentage has a negative correlation with sat scores, female percentag has a positive correlation with sat scores. None of the correlations are strong


# In[185]:


combined[combined['female_per']>60][combined['sat_score']>1700]['School Name']


# In[186]:


#they are selective liberal art schools


# In[188]:


combined['ap_per'] =combined['AP Test Takers ']/combined['total_enrollment']
combined.plot.scatter('ap_per', 'sat_score')
plt.show()


# In[189]:


#the correlation is not strong


# In[194]:


combined.corr(method='pearson')['sat_score']['AVERAGE CLASS SIZE']


# In[195]:


#there is a positive correlation between sat score and average class size


# In[197]:


combined.iloc[0]

