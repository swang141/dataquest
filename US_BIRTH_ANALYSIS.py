#!/usr/bin/env python
# coding: utf-8

# In[7]:


f = open('US_births_1994-2003_CDC_NCHS.csv')
rows = f.read()
birth_data = rows.split('\n')
print (birth_data[0:10])


# In[8]:


def read_csv(csv):
    f = open(csv)
    string = f.read()
    string_list = string.split('\n')[1:]
    final_list = []
    for row in string_list:
        string_fields = row.split(',')
        int_fields = []
        for item in string_fields:
            item = int(item)
            int_fields.append(item)
        final_list.append(int_fields) 
    return final_list
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[:10]
    



# In[26]:


def month_birth(lst):
    births_per_month = {}
    for row in lst:
        month = row[1]
        birth = row[-1]
        if month in births_per_month:
            births_per_month[month] += birth
        else:
            births_per_month[month]=birth
    return births_per_month
cdc_month_birth = month_birth(cdc_list)
cdc_month_birth


# In[9]:


def dow_births(lst):
    total_birth = {}
    for row in lst:
        dow = row[3]
        birth = row[-1]
        if dow in total_birth:
            total_birth[dow] += birth
        else:
            total_birth[dow] = birth
    return total_birth
cdc_day_births = dow_births(cdc_list)
cdc_day_births
        
        


# In[10]:


def calc_counts(data, column):
    birth_total = {}
    for row in data:
        if row[column] in birth_total:
            birth_total[row[column]] += row[-1]
        else:
            birth_total[row[column]] = row[-1]
    return birth_total
cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list,1)
cdc_dom_births = calc_counts(cdc_list,2)
cdc_dow_births = calc_counts(cdc_list,3)

print (cdc_year_births)
print (cdc_month_births)
print (cdc_dom_births)
print (cdc_dow_births)


# In[22]:


'''
I wrote the following codes to convert each number to integer in the list of list. I know my code is wrong, because final_list.append(int_fields) should be in the loop of 'for row in string_list:'. But I am wondering if I put final_list.append(int_fields) in the loop of ' for item in string_fields:', the output should be like [1994,[1994,1],[1994,1,1],[1994,1,1,6], [1994,1,1,6,8096]...]. Can anyone explain why the actual output is [[1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772]]

Here is my code:
def read_csv(csv):
    f = open(csv)
    string = f.read()
    string_list = string.split('\n')[1:]
    final_list = []
    for row in string_list:
        string_fields = row.split(',')
        int_fields = []
        for item in string_fields:
            item = int(item)
            int_fields.append(item)
            final_list.append(int_fields) 
    return final_list
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[:10]

Output:
[[1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 1, 6, 8096],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772],
 [1994, 1, 2, 7, 7772]]
'''   
    


# In[11]:


def dic_extreme(dic):
    value = []
    for key in dic:
        value.append(dic[key])
    maximum = max(value)
    minimum = min(value)
    result = [maximum, minimum]
    return result
dictionary = {'a':1,'b': 2,'c':3, 'd':1, 'e':0.9}
dic_extreme(dictionary)


# In[12]:


def birth_display(input_lst,column):
    dic  = {}
    for row in input_lst:
        dic2 = {}   #dictionary of dictionary: 当有一个主key的时候不需要construct一个空的子dictionary，直接用[][]来建。当两个key都没有的时候，才要construct一个空的子dictionary
        if row[0] in dic:
            if row[column] in dic[row[0]]:
                dic[row[0]][row[column]] += row[-1]
            else:
                dic[row[0]][row[column]] = row[-1]
        else:
            dic2[row[column]]=row[-1]
            dic[row[0]] = dic2
    return dic

def birth_change(input_lst,column):
    birth_change = {}
    dic = birth_display(input_lst,column)
    for year in dic:
        birth_column = {}
        if (year-1) in dic:
            for column_key in dic[year]:
                birth_column[column_key]= dic[year][column_key] - dic[year-1][column_key]
                birth_change[year] = birth_column
        else:
            for column_key in dic[year]:
                birth_column[column_key] =0
                birth_change[year] = birth_column
    return birth_change
birth_change(cdc_list, 3)


# In[13]:


def counts_group_by_year(ls, col):
    period_counts = {}
    for l in ls:
        key, ikey, val = l[0], l[col-1], l[4]
        if key in period_counts:
            if ikey in period_counts[key]:
                period_counts[key][ikey] += val
            else:
                period_counts[key][ikey] = val
        else:
            period_counts[key] = {
                ikey: val
            }
    return period_counts
    print (period_counts)

def year_on_year(datalist, col):
    yoy = {}
    counts = counts_group_by_year(datalist, col)
    for k, v in counts.items():
        for ik, iv in v.items():
            try:  
                count_prev = counts[k-1][ik]
                count_curr = counts[k][ik]
                diff = count_curr - count_prev
            except:
                diff = 0
            if k in yoy:
                yoy[k][ik] = diff
            else:
                yoy[k] = {
                    ik: diff
                }        
    return yoy

year_on_year(cdc_list,4)


# In[14]:


def calc_birth_across_year(list_of_lists,calc_birth_count_against,calc_against_specific):

    dict_birth_per_year={} 
    for data in list_of_lists: 
        if data[calc_birth_count_against]==calc_against_specific: 
        #only saturdays 
            birth_year=data[0] 
            no_of_births=data[4] 
            if birth_year in dict_birth_per_year: 
                dict_birth_per_year[birth_year]+=no_of_births 
            else:
                dict_birth_per_year[birth_year]=no_of_births 
    return dict_birth_per_year

birth_on_saturdays_every_year=calc_birth_across_year(cdc_list,3,6) 
print(birth_on_saturdays_every_year)


# In[16]:


def birth_display(input_lst,column):
    dic  = {}
    for row in input_lst:
        dic2 = {}
        if row[0] in dic:
            if row[column] in dic[row[0]]:
                dic[row[0]][row[column]] += row[-1]
            else:
                dic[row[0]][row[column]] = row[-1]
        else:
            dic2[row[column]]=row[-1]
            dic[row[0]] = dic2
    return dic

def birth_change(input_lst,column):
    birth_change = {}
    last_birth = 0
    dic = birth_display(input_lst,column)
    for year in dic:
        print (year)
        birth_column = {}
        for column_key in dic[year]:
            birth_column[column_key]= dic[year][column_key] - last_birth
            birth_change[year] = birth_column
            last_birth = dic[year][column_key]
    return birth_change
birth_change(cdc_list, 3)


# In[66]:


test={'a':{'b':1},
      'a1':{'b1':2}}
for a,b in test.items():
    print (a,b)


# In[15]:


f = open("US_births_2000-2014_SSA.csv",'r')
csv = f.read()
lst = csv.split('\n')
final_ssa_list =[] 
for row in lst[1:]:
    new_row = row.split(',')
    int_ssa = []
    for item in new_row:
        item = int(item)
        int_ssa.append(item)
    final_ssa_list.append(int_ssa)
final_ssa_list



# In[19]:


#print (len(cdc_list),len(final_ssa_list))
dup_list = []
uni_list = []
n = 0
for ssa_row in final_ssa_list:
    fun_uni_list = []
    for cdc_row in cdc_list:
        if ssa_row[:3] == cdc_list[:3]:
            first_3 = merged_list.append(ssa_row[:3])
            dup_list= first_3.append((ssa_row[-1]+cdc_list[ssa_raw[:3]])/2)
        else:
            fun_uni_list.append(ssa_row)
    if len(fun_uni_list) ==len(cdc_list):
       uni_list.append (ssa_row)
print (uni_list + dup_list)
        


# In[105]:


a=[[1,2,3,4],[4,6,7,8]]
b=[1,2,3,7]
b[:3] in a
print (b[:3] in a[])


# In[ ]:





# In[ ]:




